#!/bin/python3
import os
import sys

ns = ""

def start(name, path, bin, watch: bool = True):
    if len(sys.argv) > 1 and name not in sys.argv:
        return

    ext_args = []

    if watch:
        ext_args.append("--watch")

    if ns:
        print(f"NS: {ns}")
        ext_args.append(f"--namespace={ns}")

    print(name)
    os.chdir(path)
    os.system(f"pm2 start {' '.join(ext_args)} --name {name} {bin}")

if len(sys.argv) == 1:
    os.system("pm2 kill")

ns = "DisWidgets"

start("DisWSite", "/root/DisWidgets/Website", "npm -- start")
start("DisWGit", "/root/DisWidgets/GitBot", "npm -- start")

ns = "ChillCord"

start("CCWebsite", "/root/ChillCord/Website", "npm -- start")
start("CCAPI", "/root/ChillCord/API", "npm -- start")

ns = "Skynet"

start("SkyWeb", "/root/SkynetBot/", "npm -- start")

ns = "Tweeter"

start("Tweeter", "/root/Tweeter", "npm -- start")
start("TweeterWeb", "/root/Tweeter/Website", "npm -- start")

ns = "CordX"

start("CordX", "/root/CordX/OldSite", "npm -- start")

ns = "DscJobs"

start("DscJobs", "/root/DscJobs", "npm -- start")

ns = "DscJobs"

start("DscJobsAPI", "/root/DscJobsAPI", "npm -- start")

ns = "DscJobs"

start("DscJobsMod", "/root/DscJobsMod", "npm -- start")

ns = "ReviewBots"

start("ReviewBotsAPI", "/root/ReviewBots/API", "npm -- start")

ns = "ReviewBots"

start("ReviewBots", "/root/ReviewBots", "npm -- start")

ns = "Migizi"

start("MigiziWeb", "/root/MigiziWeb", "yarn -- start")

ns = "Migizi"

start("MigiziBot", "/root/MigiziBot", "yarn -- start")

ns = "ArtieAI"
start("ArtieAI", "/root/ArtieAI", "npm -- start")

ns = "CordXNew"
start("CordXNew", "/root/CordXNew", "yarn -- start:all")

