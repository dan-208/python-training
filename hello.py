#!/usr/bin/env python3

def print_several_times(input, n):
	print(input * n)

def square(x):
	return x * x

def string_length(input):
	# Your task is to write this function
	running_total=0
	for c in input:
		running_total=running_total+1
	return running_total

print_several_times("hello", 5)
print_several_times("my name is Dan ", 2)

print("5 squared is " + str(square(5)))

my_string = "hello I am Paul Bullion"
print("The length of my_string is " + str(string_length(my_string)))