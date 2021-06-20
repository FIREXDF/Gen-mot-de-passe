#!/bin/sh
import random
element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!"
passwd = ""

for i in range(25): passwd = passwd + element[random.randint(0, len(element) - 1)]
print(passwd)

