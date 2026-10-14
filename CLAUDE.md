# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A collection of independent, self-contained Python sample scripts demonstrating integration with the [Authorize.Net Python SDK](https://github.com/AuthorizeNet/sdk-python) (`authorizenet` package). Each script is a standalone example mirroring a method in the Authorize.Net API Reference Guide — there is no shared application code to build.

## Commands

Install dependencies (uv-based, see `pyproject.toml` / `uv.lock`):
```
uv sync
```

Run an individual sample directly (each script has a `__main__` guard):
```
python PaymentTransactions/charge-credit-card.py
```
Note the filenames use hyphens, so scripts cannot be imported as normal modules by path — see below.

Run the full sample suite (what CI/`.travis.yml` invokes):
```
python test-runner.py
```
`test-runner.py` is a `unittest.TestCase` where each test method loads one sample script via `SourceFileLoader(...).load_module()` (required because filenames contain hyphens and aren't valid module names) and calls its public function. Some tests chain multiple scripts together (e.g. `create_customer_payment_profile` creates a customer profile, creates a payment profile on it, then deletes the profile) to exercise realistic flows and clean up created resources afterward.

`list_of_sample_codes.txt` is a reference table of every sample function test-runner knows about, with flags for whether it depends on another sample and whether it actually hits the live API (`IsDependent`, `RunApi`) — not all are wired into `test-runner.py` yet.

## Architecture

- **`constants.py`** — shared sandbox credentials and dummy IDs (`apiLoginId`, `transactionKey`, `customerProfileId`, etc.) used across samples. Every sample script loads this via `SourceFileLoader('modulename', 'constants.py').load_module()` rather than a normal import, again because scripts are run as top-level files from the repo root, not as a package.
- **Category directories** (`PaymentTransactions/`, `CustomerProfiles/`, `RecurringBilling/`, `TransactionReporting/`, `FraudManagement/`, `MobileInAppTransactions/`, `AcceptSuite/`, `PayPalExpressCheckout/`, `VisaCheckout/`) — mirror the structure of the Authorize.Net API Reference Guide. Each file is independent; nothing imports across category directories except through `test-runner.py`'s cross-sample flows.
- **Sample script shape**: every script defines one function named after the file (e.g. `charge-credit-card.py` defines `charge_credit_card(amount)`), builds the relevant `apicontractsv1` request objects, sends it through an `apicontrollers` controller, and prints a human-readable success/error result. The function returns the raw SDK `response` object so other scripts/tests can chain off it (e.g. pulling `response.customerProfileId`). Scripts end with:
  ```python
  if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
      charge_credit_card(CONSTANTS.amount)
  ```
  so the sample both runs standalone and is safely loadable by `test-runner.py` without re-executing on import.
- **`src/sample_code_python/`** — a minimal uv-managed package scaffold (`__init__.py` with a `main()`); it is not yet wired to the sample scripts above and isn't part of the runnable sample flow.
- Credentials in `constants.py` are Authorize.Net's public sandbox test credentials, not secrets.
