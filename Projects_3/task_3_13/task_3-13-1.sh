#!/bin/bash

# Замена пути к базе данных в settings.php
sed -i 's#/var/lib/mysql/data#/mnt/ssd/mysql#g' settings.php

