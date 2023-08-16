#!/usr/bin/python3
from src.sections.main import Main
from threading import Thread, Event

if __name__ == '__main__':
    Thread(target=Main().initApp, args=()).start()