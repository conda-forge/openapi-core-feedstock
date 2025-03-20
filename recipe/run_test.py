import sys
from subprocess import call

FAIL_UNDER = 91

# added on https://github.com/conda-forge/openapi-core-feedstock/pull/22
SKIPS = [
    "test_request_response_error",
    "test_spec_invalid",
    "test_spec_not_detected",
    "test_webhook_request_validator_not_found",
    "test_spec_not_detected",
    "test_spec_not_supported",
    "test_webhook_response_validator_not_found",
]

COV = ["coverage"]
K = [f"""not ({" or ".join(SKIPS)})"""]
PYTEST = ["pytest", "-vv", "--tb=long", "--color=yes", "--asyncio-mode=auto", "-k", *K]
RUN = ["run", "--source", "openapi_core", "--branch", "-m", *PYTEST]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

if __name__ == "__main__":
    sys.exit(max([call([*COV, *RUN]), call([*COV, *REPORT])]))
