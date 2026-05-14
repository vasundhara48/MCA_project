from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm, AddSkillForm
from .models import UserProfile, UserSkill, Analysis
from .skill_data import (
    SKILL_CATEGORIES, ROLES, ALL_SKILLS,
    analyze_gap, generate_roadmap,
)


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'analyzer/home.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=email, email=email, password=password,
                first_name=full_name,
            )
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created.')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'analyzer/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, 'Welcome back!')
                    nxt = request.GET.get('next', 'dashboard')
                    return redirect(nxt)
                else:
                    form.add_error('password', 'Incorrect password.')
            except User.DoesNotExist:
                form.add_error('email', 'No account found with this email.')
    else:
        form = LoginForm()
    return render(request, 'analyzer/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def dashboard(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    user_skills = UserSkill.objects.filter(user=request.user).order_by('-added_at')
    latest_analysis = Analysis.objects.filter(user=request.user).first()

    context = {
        'profile': profile,
        'user_skills': user_skills,
        'latest_analysis': latest_analysis,
        'roles': ROLES,
    }
    return render(request, 'analyzer/dashboard.html', context)


@login_required
def add_skill(request):
    if request.method == 'POST':
        skill_name = request.POST.get('skill_name', '').strip()
        proficiency = request.POST.get('proficiency', 'intermediate')
        if skill_name:
            obj, created = UserSkill.objects.get_or_create(
                user=request.user,
                skill_name=skill_name,
                defaults={'proficiency': proficiency},
            )
            if created:
                messages.success(request, f'Added "{skill_name}" to your skills.')
            else:
                messages.info(request, f'"{skill_name}" is already in your skills.')
        else:
            messages.error(request, 'Please enter a skill name.')
    return redirect('dashboard')


@login_required
def remove_skill(request, skill_id):
    skill = get_object_or_404(UserSkill, id=skill_id, user=request.user)
    skill.delete()
    messages.success(request, f'Removed "{skill.skill_name}" from your skills.')
    return redirect('dashboard')


@login_required
def set_target_role(request):
    if request.method == 'POST':
        role = request.POST.get('target_role', '').strip()
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        profile.target_role = role
        profile.save()
        if role:
            messages.success(request, f'Target role set to "{role}".')
        else:
            messages.info(request, 'Target role cleared.')
    return redirect('dashboard')


@login_required
def analyze(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    user_skills = list(
        UserSkill.objects.filter(user=request.user).values_list('skill_name', flat=True)
    )

    if not user_skills:
        messages.warning(request, 'Please add at least one skill before analyzing.')
        return redirect('dashboard')

    if not profile.target_role:
        messages.warning(request, 'Please select a target role before analyzing.')
        return redirect('dashboard')

    result = analyze_gap(user_skills, profile.target_role)
    if result is None:
        messages.error(request, 'Could not analyze. Please try a different role.')
        return redirect('dashboard')

    analysis = Analysis.objects.create(
        user=request.user,
        target_role=profile.target_role,
        match_percentage=result['match_percentage'],
        matched_core=result['matched_core'],
        missing_core=result['missing_core'],
        matched_nice=result['matched_nice'],
        missing_nice=result['missing_nice'],
    )
    return redirect('results', analysis_id=analysis.id)


@login_required
def results(request, analysis_id):
    analysis = get_object_or_404(Analysis, id=analysis_id, user=request.user)
    context = {
        'analysis': analysis,
        'role_data': ROLES.get(analysis.target_role, {}),
    }
    return render(request, 'analyzer/results.html', context)


@login_required
def roadmap(request, analysis_id):
    analysis = get_object_or_404(Analysis, id=analysis_id, user=request.user)
    phases = generate_roadmap(
        analysis.missing_core, analysis.missing_nice, analysis.target_role
    )
    context = {
        'analysis': analysis,
        'phases': phases,
    }
    return render(request, 'analyzer/roadmap.html', context)
@login_required
def dashboard(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    user_skills = UserSkill.objects.filter(user=request.user).order_by('-added_at')
    latest_analysis = Analysis.objects.filter(user=request.user).first()
    
    # Get list of skill names already added by the user
    user_skill_names = list(user_skills.values_list('skill_name', flat=True))

    context = {
        'profile': profile,
        'user_skills': user_skills,
        'user_skill_names': user_skill_names,  # Needed for template logic
        'latest_analysis': latest_analysis,
        'roles': ROLES,
        'SKILL_CATEGORIES': SKILL_CATEGORIES,  # Needed for the browser
        'ALL_SKILLS': ALL_SKILLS,               # Needed for autocomplete JS
    }
    return render(request, 'analyzer/dashboard.html', context)

@login_required
def analysis_history(request):
    analyses = Analysis.objects.filter(user=request.user)[:10]
    context = {'analyses': analyses}
    return render(request, 'analyzer/dashboard.html', context)