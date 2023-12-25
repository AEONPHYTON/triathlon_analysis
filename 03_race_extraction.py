import pandas as pd
import os

path = "SET THE FORLDER THAT YO SAVED THE RACE EVENT EXTRACTION"
os.chdir(path)

for file in os.listdir():
    if file.endswith(".json"):
        file = f"{path}/{file}"
        # check if the code is 200 or 404, if 404 skip the file
        try:
            data_set = pd.read_json(file)

            if data_set.get('code').iloc[0] == 404:
                print(f"File {file} skipped due to code 404.")
                continue

        except ValueError as e:
            print(f"reading  error file number {file}: {e}")

        finally:
            print(file)

            # create empty list
            generated_id = []
            athlete_id = []
            athlete_first = []
            athlete_last = []
            athlete_gender = []
            dob = []
            athlete_country_id = []
            athlete_yob = []
            athlete_noc = []
            athlete_age = []
            athlete_categories = []
            position = []
            start_num = []
            prog_id = []
            event_id = []
            prog_name = []
            prog_date = []
            prog_gender = []
            prog_distance_category = []
            prog_distances = []
            prog_notes = []
            event_title = []
            event_venue = []
            event_country = []
            event_latitude = []
            event_longitude = []
            event_date = []
            event_country_noc = []
            event_region_id = []
            event_country_id = []
            event_region_name = []
            temperature_water = []
            temperature_air = []
            humidity = []
            wbgt = []
            wind = []
            weather = []
            wetsuit = []
            split_nuoto_arr = []
            split_T1_arr = []
            split_ciclismo_arr = []
            split_T2_arr = []
            split_corsa_arr = []
            tempo_nuoto_sec_arr = []
            tempo_T1_sec_arr = []
            tempo_ciclismo_sec_arr = []
            tempo_T2_sec_arr = []
            tempo_corsa_sec_arr = []
            tempo_totale_sec_arr = []
            total_time_total = []
            cat_name_categories = []
            cat_id_categories = []
            cat_parent_id_categories = []
            cat_name_specification_first = []
            cat_id_specification_first = []
            cat_parent_id_specification_first = []
            cat_name_specification_second = []
            cat_id_specification_second = []
            cat_parent_id_specification_second = []
            swim_distance = []
            bike_distance = []
            run_distance = []
            percentage_swim = []
            percentage_t_1 = []
            percentage_bike = []
            percentage_t_2 = []
            percentage_run = []
            swim_T1_percentage = []
            swim_T1_bike_percentage = []
            swim_T1_bike_T2_percentage = []
            avg_swim_vel = []
            avg_bike_vel = []
            avg_run_vel = []
            swim_T1 = []
            swim_T1_bike = []
            swim_T1_bike_T2 = []

            # open file
            event = data_set
            data = event["data"]
            event = data["event"]
            result = data["results"]
            length = len(result)

            # select data
            event_categorie = event["event_categories"]
            event_categorie_len = len(event_categorie)

            if event_categorie_len < 1:
                substitute_it = {
                    "cat_name": "Race",
                    "cat_id": 111,
                    "cat_parent_id": "null"
                }
                event["event_categories"] = [substitute_it]

            tipo_evento = event["event_specifications"]
            tipo_evento_len = len(tipo_evento)

            if tipo_evento_len < 1:
                dict_tipo_evento = [{
                    "cat_name": "Triathlon",
                    "cat_id": 357,
                    "cat_parent_id": "null"
                },
                {
                    "cat_name": "anonimus",
                    "cat_id": 357,
                    "cat_parent_id": "null"
                }]

                event["event_specifications"] = dict_tipo_evento

            event_specifications_type_of_race = event["event_specifications"][0]
            event_specifications_type_of_race_triathlon = event_specifications_type_of_race["cat_name"]
            prog_name_identification = data["prog_name"]
            if event_specifications_type_of_race_triathlon != "Triathlon" or "Relay" in prog_name_identification \
                    or "Team" in prog_name_identification or "Para" in prog_name_identification\
                    or "Mixed" in prog_name_identification:
                pass
            else:
                for n in range(0, length):
                    result = data["results"][n]
                    athlete_id.append(result["athlete_id"])
                    athlete_first.append(result["athlete_first"])
                    athlete_last.append(result["athlete_last"])
                    athlete_gender.append(result["athlete_gender"])

                    if "dob" not in result:
                        month = 12
                        day = 25
                        date_birth = result["athlete_yob"]
                        date_values = f'{date_birth}-{month}-{day}'
                        result["dob"] = date_values

                        data_evento = data["prog_date"]
                        data_evento_split = data_evento.split("-")[0]

                        result["athlete_age"] = int(date_birth) - int(data_evento_split)

                    dob.append(result["dob"])

                    athlete_country_id.append(result["athlete_country_id"])
                    athlete_yob.append(result["athlete_yob"])
                    athlete_noc.append(result["athlete_noc"])
                    athlete_age.append(result["athlete_age"])

                    athlete_categories.append(str(result["athlete_categories"])[1:-1])
                    position.append(result["position"])
                    start_num.append(result["start_num"])
                    split_nuoto_arr.append(result["splits"][0])
                    split_T1_arr.append(result["splits"][1])
                    split_ciclismo_arr.append(result["splits"][2])
                    split_T2_arr.append(result["splits"][3])
                    split_corsa_arr.append(result["splits"][4])
                    total_time_total.append(result["total_time"])

                    splinter = result
                    split_nuoto = splinter["splits"][0]
                    if split_nuoto == "null" or split_nuoto is None or split_nuoto == "" or split_nuoto == "DNF"\
                            or split_nuoto == "n\/a" or split_nuoto == "n/a" or split_nuoto == "0":
                        split_nuoto = "00:00:00"

                    splitting_nuoto = split_nuoto.split(":")
                    nuoto_ore_sec = int(splitting_nuoto[0]) * 3600
                    nuoto_min_sec = int(splitting_nuoto[1]) * 60
                    nuoto_sec = int(splitting_nuoto[2])
                    tempo_nuoto_sec = (nuoto_ore_sec + nuoto_min_sec + nuoto_sec)
                    tempo_nuoto_sec_arr.append(tempo_nuoto_sec)

                    # split T1 segment
                    split_T1 = splinter["splits"][1]
                    if split_T1 == "null" or split_T1 is None or split_T1 == "0" or split_T1 == "" or split_T1 == "DNF"\
                            or split_T1 == "n\/a" or split_T1 == "n/a" or split_T1 == "0":
                        split_T1 = "00:00:00"

                    splitting_T1 = split_T1.split(":")
                    T1_ore_sec = int(splitting_T1[0]) * 3600
                    T1_min_sec = int(splitting_T1[1]) * 60
                    T1_sec = int(splitting_T1[2])
                    tempo_T1_sec = (T1_ore_sec + T1_min_sec + T1_sec)
                    tempo_T1_sec_arr.append(tempo_T1_sec)

                    # split bike segment
                    split_ciclismo = splinter["splits"][2]
                    if split_ciclismo == "null" or split_ciclismo is None or split_ciclismo == "" \
                            or split_ciclismo == "DNF" or split_ciclismo == "n\/a" or split_ciclismo == "n/a"\
                            or split_ciclismo == "0":
                        split_ciclismo = "00:00:00"

                    splitting_ciclismo = split_ciclismo.split(":")
                    ciclismo_ore_sec = int(splitting_ciclismo[0]) * 3600
                    ciclismo_min_sec = int(splitting_ciclismo[1]) * 60
                    ciclismo_sec = int(splitting_ciclismo[2])
                    tempo_ciclismo_sec = (ciclismo_ore_sec + ciclismo_min_sec + ciclismo_sec)
                    tempo_ciclismo_sec_arr.append(tempo_ciclismo_sec)

                    # time for the transition 2 segment
                    split_T2 = splinter["splits"][3]
                    if split_T2 == "null" or split_T2 is None or split_T2 == "0" or split_T2 == "" or split_T2 == "DNF"\
                            or split_T2 == "n\/a" or split_T2 == "n/a" or split_T2 == "0":
                        split_T2 = "00:00:00"

                    splitting_T2 = split_T2.split(":")
                    T2_ore_sec = int(splitting_T2[0]) * 3600
                    T2_min_sec = int(splitting_T2[1]) * 60
                    T2_sec = int(splitting_T2[2])
                    tempo_T2_sec = (T2_ore_sec + T2_min_sec + T2_sec)
                    tempo_T2_sec_arr.append(tempo_T2_sec)

                    # time for the run segment
                    split_corsa = splinter["splits"][4]
                    if split_corsa == "null" or split_corsa is None or split_corsa == "" or split_corsa == "DNF"\
                            or split_corsa == "n\/a" or split_corsa == "n/a" or split_corsa == "0":
                        split_corsa = "00:00:00"

                    splitting_corsa = split_corsa.split(":")
                    corsa_ore_sec = int(splitting_corsa[0]) * 3600
                    corsa_min_sec = int(splitting_corsa[1]) * 60
                    corsa_sec = int(splitting_corsa[2])
                    tempo_corsa_sec = (corsa_ore_sec + corsa_min_sec + corsa_sec)
                    tempo_corsa_sec_arr.append(tempo_corsa_sec)

                    splinter = result
                    total_time = splinter["total_time"]

                    if total_time == "DNF" or total_time == "DNS" or total_time == "LAP" \
                            or total_time == "DSQ" or total_time == "NC" or total_time == "NE" or total_time is None \
                            or "pts" in total_time or total_time == "n\/a" or total_time == "" or total_time == "n/a"\
                            or total_time == "0" or "pts" in total_time or "pt" in total_time:
                        total_time = "00:00:00"

                    splitting_total_time = total_time.split(":")
                    total_time_ore_sec = int(splitting_total_time[0]) * 3600
                    total_time_min_sec = int(splitting_total_time[1]) * 60
                    total_time_sec_sec = int(splitting_total_time[2])
                    total_time_sec = (total_time_ore_sec + total_time_min_sec + total_time_sec_sec)
                    tempo_totale_sec_arr.append(total_time_sec)

                    # find the time sum for every split, swim + T1
                    swim_T1_sum = (tempo_nuoto_sec + tempo_T1_sec)
                    swim_T1.append(swim_T1_sum)
                    # time swim + T1 + bike
                    swim_T1_bike_sum = (tempo_nuoto_sec + tempo_T1_sec + tempo_ciclismo_sec)
                    swim_T1_bike.append(swim_T1_bike_sum)
                    # time swim + T1 + bike+ T2
                    swim_T1_bike_T2_sum = (tempo_nuoto_sec + tempo_T1_sec + tempo_ciclismo_sec + tempo_T2_sec)
                    swim_T1_bike_T2.append(swim_T1_bike_T2_sum)

                    # race information
                    prog_id.append(data["prog_id"])
                    event_id.append(data["event_id"])
                    prog_name.append(data["prog_name"])
                    prog_date.append(data["prog_date"])
                    prog_gender.append(data["prog_gender"])
                    prog_distance_category.append(data["prog_distance_category"])
                    prog_distances.append(data["prog_distances"])
                    prog_notes.append(data["prog_notes"])

                    id_plus = (str(result["athlete_id"]) +
                               str(data["prog_id"]) +
                               str(data["event_id"]))
                    generated_id.append(id_plus)


                    # event information
                    event_title.append(event["event_title"])
                    event_venue.append(event["event_venue"])
                    event_country.append(event["event_country"])
                    event_latitude.append(event["event_latitude"])
                    event_longitude.append(event["event_longitude"])
                    event_date.append(event["event_date"])
                    event_country_noc.append(event["event_country_noc"])
                    event_region_id.append(event["event_region_id"])
                    event_country_id.append(event["event_country_id"])
                    event_region_name.append(event["event_region_name"])

                    # type of triathlon event

                    event_categories = event["event_categories"][0]
                    cat_name_categories.append(event_categories["cat_name"])
                    cat_id_categories.append(event_categories["cat_id"])
                    cat_parent_id_categories.append(event_categories["cat_parent_id"])

                    # find the length of event specification

                    event_specifications_length = len(event["event_specifications"])

                    if event_specifications_length > 0:
                        event_specifications_first = event["event_specifications"][0]
                        cat_name_specification_first.append(event_specifications_first["cat_name"])
                        cat_id_specification_first.append(event_specifications_first["cat_id"])
                        cat_parent_id_specification_first.append(event_specifications_first["cat_parent_id"])

                    if event_specifications_length < 2:
                        event["event_specifications"].append({
                            "cat_name": "Sprint",
                            "cat_id": 377,
                            "cat_parent_id": 357
                        })

                    event_specifications_second = event["event_specifications"][1]
                    cat_name_specification_second.append(event_specifications_second["cat_name"])
                    cat_id_specification_second.append(event_specifications_second["cat_id"])
                    cat_parent_id_specification_second.append(event_specifications_second["cat_parent_id"])

                    # race distances

                    cat_name_dist = event_specifications_second["cat_name"]

                    if cat_name_dist == "Standard":
                        swim_dist = "1500"
                        bike_dist = "40000"
                        run_dist = "10000"
                    elif cat_name_dist == "Sprint":
                        swim_dist = "750"
                        bike_dist = "20000"
                        run_dist = "5000"
                    elif cat_name_dist == "Mixed Relay":
                        swim_dist = "400"
                        bike_dist = "8000"
                        run_dist = "2500"
                    elif cat_name_dist == "Super Sprint":
                        swim_dist = "400"
                        bike_dist = "10000"
                        run_dist = "2500"
                    elif cat_name_dist == "anonimus":
                        swim_dist = "0"
                        bike_dist = "0"
                        run_dist = "0"

                    swim_distance.append(swim_dist)
                    bike_distance.append(bike_dist)
                    run_distance.append(run_dist)

                    # percentage of the sector
                    try:
                        percentage_swim_cal = ("%.2f" % float((tempo_nuoto_sec / total_time_sec) * 100))
                        percentage_t_1_cal = ("%.2f" % float((tempo_T1_sec / total_time_sec) * 100))
                        percentage_bike_cal = ("%.2f" % float((tempo_ciclismo_sec / total_time_sec) * 100))
                        percentage_t_2_cal = ("%.2f" % float((tempo_T2_sec / total_time_sec) * 100))
                        percentage_run_cal = ("%.2f" % float((tempo_corsa_sec / total_time_sec) * 100))
                    except ZeroDivisionError:
                        percentage_swim_cal = 0.00
                        percentage_t_1_cal = 0.00
                        percentage_bike_cal = 0.00
                        percentage_t_2_cal = 0.00
                        percentage_run_cal = 0.00

                    percentage_swim.append(percentage_swim_cal)
                    percentage_t_1.append(percentage_t_1_cal)
                    percentage_bike.append(percentage_bike_cal)
                    percentage_t_2.append(percentage_t_2_cal)
                    percentage_run.append(percentage_run_cal)

                    # find the percentage of the sum of the split
                    try:
                        swim_T1_sum_percentage = ("%.2f" % (float(swim_T1_sum / total_time_sec) * 100))
                        swim_T1_bike_sum_percentage = ("%.2f" % (float(swim_T1_bike_sum / total_time_sec) * 100))
                        swim_T1_bike_T2_sum_percentage = ("%.2f" % (float(swim_T1_bike_T2_sum / total_time_sec) * 100))
                    except ZeroDivisionError:
                        swim_T1_sum_percentage = 0.00
                        swim_T1_bike_sum_percentage = 0.00
                        swim_T1_bike_T2_sum_percentage = 0.00

                    swim_T1_percentage.append(swim_T1_sum_percentage)
                    swim_T1_bike_percentage.append(swim_T1_bike_sum_percentage)
                    swim_T1_bike_T2_percentage.append(swim_T1_bike_T2_sum_percentage)

                    # average velocity of the split
                    try:
                        if cat_name_dist == "Standard":
                            avg_swim_vel_cal = ("%.2f" % float(1500 / tempo_nuoto_sec))
                            avg_bike_vel_cal = ("%.2f" % float(40000 / tempo_ciclismo_sec))
                            avg_run_vel_cal = ("%.2f" % float(10000 / tempo_corsa_sec))
                        elif cat_name_dist == "Sprint":
                            avg_swim_vel_cal = ("%.2f" % float(750 / tempo_nuoto_sec))
                            avg_bike_vel_cal = ("%.2f" % float(20000 / tempo_ciclismo_sec))
                            avg_run_vel_cal = ("%.2f" % float(5000 / tempo_corsa_sec))
                        elif cat_name_dist == "Mixed Relay":
                            avg_swim_vel_cal = ("%.2f" % float(400 / tempo_nuoto_sec))
                            avg_bike_vel_cal = ("%.2f" % float(8000 / tempo_ciclismo_sec))
                            avg_run_vel_cal = ("%.2f" % float(2500 / tempo_corsa_sec))
                        elif cat_name_dist == "Super Sprint":
                            avg_swim_vel_cal = ("%.2f" % float(400 / tempo_nuoto_sec))
                            avg_bike_vel_cal = ("%.2f" % float(10000 / tempo_ciclismo_sec))
                            avg_run_vel_cal = ("%.2f" % float(2500 / tempo_corsa_sec))
                    except ZeroDivisionError:
                        avg_swim_vel_cal = 0.00
                        avg_bike_vel_cal = 0.00
                        avg_run_vel_cal = 0.00

                    avg_swim_vel.append(avg_swim_vel_cal)
                    avg_bike_vel.append(avg_bike_vel_cal)
                    avg_run_vel.append(avg_run_vel_cal)

                    # meteo information about race
                    meteo = data["meta"]
                    temperature_water.append(meteo["temperature_water"])
                    temperature_air.append(meteo["temperature_air"])
                    humidity.append(meteo["humidity"])
                    wbgt.append(meteo["wbgt"])
                    wind.append(meteo["wind"])
                    weather.append(meteo["weather"])
                    wetsuit.append(meteo["wetsuit"])

                # write dataframe

                dataframe = {
                    "generated_id": generated_id,
                    "athlete_id": athlete_id,
                    "prog_id": prog_id,
                    "event_id": event_id,
                    "athlete_first": athlete_first,
                    "athlete_last": athlete_last,
                    "athlete_gender": athlete_gender,
                    "dob": dob,
                    "athlete_country_id": athlete_country_id,
                    "athlete_yob": athlete_yob,
                    "athlete_noc": athlete_noc,
                    "athlete_age": athlete_age,
                    "athlete_categories": athlete_categories,
                    "prog_name": prog_name,
                    "prog_date": prog_date,
                    "prog_gender": prog_gender,
                    "prog_distance_category": prog_distance_category,
                    "prog_distances": prog_distances,
                    "prog_notes": prog_notes,
                    "cat_name_categories": cat_name_categories,
                    "cat_id_categories": cat_id_categories,
                    "cat_parent_id_categories": cat_parent_id_categories,
                    "cat_name_specification_first": cat_name_specification_first,
                    "cat_id_specification_first": cat_id_specification_first,
                    "cat_parent_id_specification_first": cat_parent_id_specification_first,
                    "cat_name_specification_second": cat_name_specification_second,
                    "cat_id_specification_second": cat_id_specification_second,
                    "cat_parent_id_specification_second": cat_parent_id_specification_second,
                    "event_title": event_title,
                    "event_venue": event_venue,
                    "event_country": event_country,
                    "event_latitude": event_latitude,
                    "event_longitude": event_longitude,
                    "event_date": event_date,
                    "event_country_noc": event_country_noc,
                    "event_region_id": event_region_id,
                    "event_country_id": event_country_id,
                    "event_region_name": event_region_name,
                    "temperature_water": temperature_water,
                    "temperature_air": temperature_air,
                    "humidity": humidity,
                    "wbgt": wbgt,
                    "wind": wind,
                    "weather": weather,
                    "wetsuit": wetsuit,
                    "position": position,
                    "start_num": start_num,
                    "split_nuoto": split_nuoto_arr,
                    "split_T1": split_T1_arr,
                    "split_ciclismo": split_ciclismo_arr,
                    "split_T2": split_T2_arr,
                    "split_corsa": split_corsa_arr,
                    "total_time": total_time_total,
                    "tempo_nuoto_sec": tempo_nuoto_sec_arr,
                    "tempo_T1_sec": tempo_T1_sec_arr,
                    "tempo_ciclismo_sec": tempo_ciclismo_sec_arr,
                    "tempo_T2_sec": tempo_T2_sec_arr,
                    "tempo_corsa_sec": tempo_corsa_sec_arr,
                    "tempo_totale_sec": tempo_totale_sec_arr,
                    "swim_T1": swim_T1,
                    "swim_T1_bike": swim_T1_bike,
                    "swim_T1_bike_T2": swim_T1_bike_T2,
                    "swim_distance": swim_distance,
                    "bike_distance": bike_distance,
                    "run_distance": run_distance,
                    "percentage_swim": percentage_swim,
                    "percentage_t_1": percentage_t_1,
                    "percentage_bike": percentage_bike,
                    "percentage_t_2": percentage_t_2,
                    "percentage_run": percentage_run,
                    "swim_T1_percentage": swim_T1_percentage,
                    "swim_T1_bike_percentage": swim_T1_bike_percentage,
                    "swim_T1_bike_T2_percentage": swim_T1_bike_T2_percentage,
                    "avg_swim_vel_m/s": avg_swim_vel,
                    "avg_bike_vel_m/s": avg_bike_vel,
                    "avg_run_vel_m/s": avg_run_vel
                }

                # write file, select the folder that you want to save the file
                df = pd.DataFrame(dataframe)
                df.to_csv("race_result.csv", mode="a", header=False, index=False)
