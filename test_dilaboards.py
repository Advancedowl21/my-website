"""
Quick test to check if dilaboards.com is accessible
"""
import socket
import requests

print("=" * 70)
print("TESTING DILABOARDS.COM CONNECTIVITY")
print("=" * 70)

# Test 1: DNS Resolution
print("\n[TEST 1] DNS Resolution")
try:
    ip = socket.gethostbyname('dilaboards.com')
    print(f"✓ DNS resolved: dilaboards.com -> {ip}")
except socket.gaierror as e:
    print(f"✗ DNS failed: {e}")
    print("\nExiting - cannot resolve domain")
    exit(1)

# Test 2: HTTP Connection
print("\n[TEST 2] HTTP Connection Test")
test_url = 'https://dilaboards.com'
try:
    response = requests.get(test_url, timeout=10)
    print(f"✓ Connection successful: Status {response.status_code}")
except requests.exceptions.Timeout:
    print(f"✗ Timeout: Server took too long to respond")
except requests.exceptions.ConnectionError as e:
    print(f"✗ Connection error: {e}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 3: Specific path
print("\n[TEST 3] Testing Target Path")
test_path = 'https://dilaboards.com/en/moj-racun/add-payment-method/'
try:
    response = requests.get(test_path, timeout=10, allow_redirects=True)
    print(f"✓ Path accessible: Status {response.status_code}")
    print(f"  Final URL: {response.url}")
except requests.exceptions.Timeout:
    print(f"✗ Timeout: Path took too long to respond")
except requests.exceptions.ConnectionError as e:
    print(f"✗ Connection error: {e}")
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
