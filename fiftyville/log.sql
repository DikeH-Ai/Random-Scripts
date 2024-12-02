-- Keep a log of any SQL queries you execute as you solve the mystery.

--list of all tables
-- airports              crime_scene_reports   people
--atm_transactions      flights               phone_calls
--bakery_security_logs  interviews
--bank_accounts         passengers

--step one, dive into crime_scene_reports.
SELECT *  FROM crime_scene_reports; --to get a general feel of how the table structure.
SELECT *  FROM crime_scene_reports WHERE month = 7 AND  day = 28 AND year = 2021 AND street = 'Humphrey Street';  --query for information on what occured on the said day. produced 2 results.
SELECT *  FROM crime_scene_reports WHERE month = 7 AND  day = 28 AND year = 2021 AND street = 'Humphrey Street' AND id = 295; --narrowed down to our crime of interest.
--note
--time = 10:15, witnesses, bakery, interview-transcripts
--step 2 , dive into the interviews taken on that day
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 --query for information from the interview table. again multiple results.
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%' OR '%thief%'; --narrow down based on subjects.
--note
/*Ruth saw the thief leaving the bakery through its parking lot within 10 mins of the thieft,his carwas parked there: he came with a car.
CHECK THE security footage for cars that left with the time frame*\
--Eugene had seen the thief earlier this morning withdrawing money from an ATM on leggett street
--Raymond heard the thief make contact with hes accomplice plannin to take the earliest flight out of fiftyville tomorrow, the thief asked the person 
