SETLOCAL enableextensions enabledelayedexpansion 
@echo off

echo -----------------------
echo Spectate Script (Copied bunch from OP.GG spectate) 
echo -----------------------
d:
set RADS_PATH=D:\Program Files (x86)\Riot Games\League of Legends

if exist "%RADS_PATH%\Game" (
	cd /d "!RADS_PATH!\Config"
	for /F "delims=" %%a in ('find "        locale: " LeagueClientSettings.yaml') do set "locale=%%a"
	for /F "tokens=2 delims=: " %%a in ("!locale!") do set "locale=%%a"

	SET RADS_PATH="!RADS_PATH!\Game"
	@cd /d !RADS_PATH!

	if exist "League of Legends.exe" (
		@start "" "League of Legends.exe" "spectator spectator.na2.lol.riotgames.com:80 Rx4KRjBT+yANEOZd/WRmYFyndbgcilrA 3775418246 NA1" "-UseRads" "-Locale=!locale!" "-GameBaseDir=.."
		goto :eof
	)
)
@pause

:eof