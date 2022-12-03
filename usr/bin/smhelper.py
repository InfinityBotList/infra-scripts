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

ns = "Infinity"

start("InfinityBotList", "/root/InfinityBotList/MainSite", "npm -- start")
start("ManagerBot", "/root/InfinityBotList/InfinityManager", "npm -- start")
start("PopplioLegacy", "/root/Popplio", "process.json", watch=False)
start("Popplio", "/root/Popplio-V2", "process.json", watch=False)
start("Artemis", "/root/Artemis", "process.json", watch=False)
start("ArcadiaBot", "/root/arcadia/bot", "process.json", watch=False)
start("ArcadiaAPI", "/root/arcadia/api", "process.json", watch=False)
start("TicketPanelServer", "/root/InfinityBotList/TicketPanel/server", "npm -- start")
start("TicketPanelTranscripts", "/root/InfinityBotList/TicketPanel/transcripts", "npm -- start")
start("Reedwhisker", "/root/InfinityBotList/Infinity-Next", "npm -- start")
start("BlogSiteIBL", "/root/InfinityBotList/BlogSite", "yarn -- serve")
start("GithubIBL", "/root/InfinityBotList/GithubBot", "npm -- start")
start("AppSiteIBL", "/root/InfinityBotList/AppsSite", "npm -- start")
start("IBLTicket", "/root/InfinityBotList/TicektBot", "npm -- start")
start("BaseProxy", "/root/proxysid", "process.json", watch=False)
start("TSWeb", "/root/ts-webhook-adapter", "process.json", watch=False)

ns = "DisWidgets"

start("DisWSite", "/root/DisWidgets/Website", "npm -- start")
start("DisWGit", "/root/DisWidgets/GitBot", "npm -- start")

ns = "ChillCord"

start("CCWebsite", "/root/ChillCord/Website", "npm -- start")
start("CCAPI", "/root/ChillCord/API", "npm -- start")

ns = "ToxMod"

start("ToxWeb", "/root/ToxMod/Website", "npm -- start")
start("ToxAPI", "/root/ToxMod/API", "npm -- start")

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

ns = "ToxModBeta"

start("ToxModBeta", "/root/ToxMod/BetaSite", "yarn -- start")

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

