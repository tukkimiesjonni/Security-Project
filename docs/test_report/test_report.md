# Testing Document

## 1. Unit Test Coverage Report

| Name                                | Stmts | Miss | Branch | BrPart | Cover | Missing |
|-------------------------------------|-------|------|--------|--------|--------|---------|
| src/crypt/__init__.py              | 0     | 0    | 0      | 0      | 100%   |         |
| src/crypt/decryption.py            | 9     | 0    | 2      | 0      | 100%   |         |
| src/crypt/encryption.py            | 10    | 0    | 6      | 0      | 100%   |         |
| src/keys/__init__.py               | 0     | 0    | 0      | 0      | 100%   |         |
| src/keys/key_generation.py         | 10    | 0    | 2      | 1      | 92%    | 33→29   |
| src/tests/__init__.py              | 0     | 0    | 0      | 0      | 100%   |         |
| src/tests/test_decryption.py       | 18    | 0    | 0      | 0      | 100%   |         |
| src/tests/test_encryption.py       | 19    | 0    | 0      | 0      | 100%   |         |
| src/tests/test_key_generation.py   | 39    | 0    | 0      | 0      | 100%   |         |
| src/tests/test_utils.py            | 63    | 1    | 2      | 1      | 97%    | 160     |
| src/util_functions/__init__.py     | 0     | 0    | 0      | 0      | 100%   |         |
| src/util_functions/primes.py       | 1     | 0    | 0      | 0      | 100%   |         |
| src/util_functions/utils.py        | 46    | 0    | 20     | 0      | 100%   |         |
| **TOTAL**                          | 215   | 1    | 32     | 2      | **99%**|         |


## 2. What Was Tested and How?

The `encryption.py` and `decryption.py` modules were tested using unit tests with various inputs. Additionally, all functions in `utils.py` were tested with appropriate inputs. The functions in `key_generation.py` were also tested with valid inputs.

## 3. What Kind of Inputs Were Used for Testing?

The functions were tested with both valid and invalid inputs. Valid inputs ranged from small to large values.

## 4. How Can the Tests Be Reproduced?

This is explained in the README.

---