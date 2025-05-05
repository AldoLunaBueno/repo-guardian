# features/steps/scan_steps.py

from behave import given, when, then
import subprocess
from pathlib import Path


@given('un repositorio con packfile "{repo_path}"')
def step_given_packfile_repo(context, repo_path):
    context.repo_path = Path(repo_path)
    assert context.repo_path.exists(), f"Fixture {repo_path} not found"


@when('ejecuto "guardian scan {repo_path}"')
def step_when_run_guardian_scan(context, repo_path):
    result = subprocess.run(
        ["guardian", "scan", repo_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    context.exit_code = result.returncode
    context.stdout = result.stdout
    context.stderr = result.stderr


@then("el exit code es {code:d}")
def step_then_exit_code_is(context, code):
    assert context.exit_code == code, f"Exit code was {context.exit_code}, \
        expected {code}"


@then('la salida contiene "{text}"')
def step_then_output_contains(context, text):
    assert text in context.stderr or text in context.stdout, "Output \
        does not contain '{text}'"
