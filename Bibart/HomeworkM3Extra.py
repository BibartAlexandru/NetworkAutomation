from ConfigureEnvironment import configure_environment
from TestGuestPing import test_ping
configure_environment()
res = test_ping()
if res == True:
    print("Ping from Guest to Server succeeded")
else:
    print("Ping from Guest to Server failed")