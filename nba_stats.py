from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

seasons = ["2021-22", "2020-21", "2019-20", "2018-19", "2017-18", "2016-17", "2015-16",
           "2014-15", "2013-14", "2012-13", "2011-12", "2010-11", "2009-10", "2008-09",
           "2007-08", "2006-07", "2005-06", "2004-05", "2003-04", "2002-03", "2001-02",
           "2000-01", "1999-00", "1998-99", "1997-98", "1996-97"]
season_types = ["Pre+Season", "Regular+Season",
                "Playoffs", "All+Star", "PlayIn"]
permodes = ["Totals", "PerGame", "Per100Possessions", "Per100Plays", "Per48",
            "Per40", "Per36", "PerMinute", "PerPossession", "PerPlay", "MinutesPer"]
sorts = ["TEAM_ABBREVIATION", "AGE", "W", "L", "MIN", "PTS", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA",
         "FT_PCT", "OREB", "DREB", "REB", "AST", "TOV", "STL", "BLK", "PF", "NBA_FANTASY_PTS", "DD2", "TD3", "PLUS_MINUS"]

# scrape mechanic


def scrape_nbastats():
    driver = webdriver.Chrome(service=Service("chromedriver"))

    filename = f'stats&s{season.get()}&type{season_type.get()}&permode{permode.get()}&sort{sort.get()}.csv'
    driver.get(
        f"https://www.nba.com/stats/players/traditional?PerMode={permode.get()}&Season={season.get()}&SeasonType={season_type.get()}&dir=A&sort={sort.get()}")

    header_list = [header.text for header in driver.find_elements(
        By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th') if header.text != '']
    player_list = []
    rows = driver.find_elements(
        By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody/tr')
    for row in range(len(rows)):
        tds = rows[row].find_elements(
            By.XPATH, f'//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody/tr[{row}]/td')
        td_list = [td.text for td in tds]
        player_list.append(td_list)

    with open(f'finished-projects/81-100. [PRO]/92. [Web Scraping] Custom Web Scraper/{filename}', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header_list)
        writer.writerows(player_list)
    messagebox.showinfo("Done!", f"Your file was saved by name of: {filename}")


# UI
master = Tk()
master.config(padx=50, pady=50)


season = StringVar(master)
season_type = StringVar(master)
permode = StringVar(master)
sort = StringVar(master)
season.set(seasons[0])
season_type.set(season_types[0])
permode.set(permodes[0])
sort.set(sorts[0])

season_options = OptionMenu(master, season, *seasons)
season_type_options = OptionMenu(master, season_type, *season_types)
permode_options = OptionMenu(master, permode, *permodes)
sort_options = OptionMenu(master, sort, *sorts)
submit_button = Button(master, text='Start', command=scrape_nbastats)
season_label = Label(master, text='Season')
season_type_label = Label(master, text='Season Type')
permode_label = Label(master, text='Per Mode')
sort_label = Label(master, text='Sort by')

season_label.grid(column=0, row=0)
season_type_label.grid(column=1, row=0)
permode_label.grid(column=2, row=0)
sort_label.grid(column=3, row=0)
season_options.grid(column=0, row=1, sticky='EW')
season_type_options.grid(column=1, row=1, sticky='EW')
permode_options.grid(column=2, row=1, sticky='EW')
sort_options.grid(column=3, row=1, sticky='EW')
submit_button.grid(column=0, row=4, columnspan=4)

mainloop()
