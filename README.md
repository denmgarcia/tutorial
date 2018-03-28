This script runs on terminal - means you have to run script with additional flag otherwise it fails.

Running python convert.py --help will give you an idea whats the option available

convert.py script helps you to convert given temperature to celsius or farenheit vice versa.

Example:

$ python convert.py --farenheit 32

should echo 0.0 C since it is now converted to celsius 0.0C == 32F

[x] Celsius  
[x] Farenheit  
[ ] Kelvin  

------------------------------------------
Script uses the power of sys.argv it creates a simple folder using the flag you specified

$ python argv.py --create myFolder # myFolder is created

When running in ordinary user it throws an error, otherwise root is working just fine
and also --delete flag has ability to delete directory in ordinary user mode


 
