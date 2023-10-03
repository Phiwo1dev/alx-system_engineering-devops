0x06-regular_expressions - Project by ALX_SWE
==============================================

Background Context
===================
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

Tasks
======
0. Simply matching School

Requirements:

-The regular expression must match School
-Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

1. Repetition Token #0

Requirements:

-Find the regular expression that will match the above cases
-Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

2. Repetition Token #1

Requirements:

-Find the regular expression that will match the above cases
-Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

3. Repetition Token #2

Requirements:

-Find the regular expression that will match the above cases
-Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

4. Repetition Token #3

Requirements:

-Find the regular expression that will match the above cases
-Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
-Your regex should not contain square brackets

5. Not quite HBTN yet

Requirements:

-The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
-Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

6. Call me maybe

This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

Requirement:

-The regular expression must match a 10 digit phone number

7. OMG WHY ARE YOU SHOUTING?

Requirement:

-The regular expression must be only matching: capital letters

8. Textme

This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

-Your script should output: [SENDER],[RECEIVER],[FLAGS]
-The sender phone number or name (including country code if present)
-The receiver phone number or name (including country code if present)
-The flags that were used
-You can find a [log file here].

====================================================================================================================================================
