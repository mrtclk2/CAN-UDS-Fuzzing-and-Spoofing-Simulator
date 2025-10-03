
# Example Scenarios

## Scenario 1 – Brute Force SID

This script (`scenario1_bruteforce_sid.py`) iterates over all possible UDS Service IDs (0x00–0xFF)  
and sends randomized payloads. Useful for discovering undocumented services or triggering ECU responses.

Future scenarios could include:
- ReadDataByIdentifier targeting (0x22)
- WriteDataByIdentifier (0x2E)
- DiagnosticSessionControl modes (0x10)
