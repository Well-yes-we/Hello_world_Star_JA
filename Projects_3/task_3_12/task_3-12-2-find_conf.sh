#!/bin/bash

# Вывод файлов .conf из /etc (регистронезависимо)
ls -l /etc | grep -i "\.conf$"

