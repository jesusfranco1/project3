import urllib.request
import json
#import dml
import prov.model
import datetime
import uuid
class crimerate():
    contributor = 'lc546_jofranco'
    #reads = []
    #writes = ['lc546_jofranco.crimerate']
    @staticmethod
    def execute(trial = False):
        startTime = datetime.datetime.now()
         #Set up the database connection.
    #    client = dml.pymongo.MongoClient()
    #    repo = client.repo
    #    repo.authenticate("lc546_jofranco", "lc546_jofranco")
    #    url = 'https://data.boston.gov/export/12c/b38/12cb3883-56f5-47de-afa5-3b1cf61b257b.json'
        #response = urllib.request.urlopen(url).read().decode("utf-8")
        response = open('/Users/Jesus/Desktop/project3/project3/crimeratetext.txt').read()
        responsetext = open("fixedcrimes.txt", "w")
        crimesfinal = open("crimes.txt", "w")

        #print('######')
        #print(response)
        #response = json.dumps(response)
        #print(response)
        #response.replace("", ' ')
        #print(response)
        #for i in response:
        #    print(i)
        r = json.loads(response)
        #print(r['crimes'])
        crime_coordinates = []
        for i in r['crimes']:
            if str(i['Location']) != '(-1.00000000, -1.00000000)' and str(i['Location']) != '(0.00000000, 0.00000000)':
                coordinate1 = str(i['Location'])
                coordinate2 = coordinate1.replace('(', '[')
                coordinate3 = coordinate2.replace(')', ']')
                #print(str(coordinate3))
                #print(str(i['Location']))
                crime_coordinates.append(coordinate3)

        coordinates_for_heatmap = []
        crimesfinal.write("var addressPoints = [")
        count = 0
        for i in crime_coordinates:
            lat0 = i[1:14]
            log0 = i[15:-1]
            sums = 0

            for j in crime_coordinates:
                lat = j[1:14]
                log = j[15:-1]
                difflat = abs(float(lat.replace(",","")) - float(lat0.replace(",", "")))
                difflog = abs(float(log) - float(log0))
                if (difflat <= .01) and (difflog <= .01):
                    sums += 1
                #print(difflat, difflog)
            if count == 0:
                pointlatlong = '[' + str(lat0.replace(",","")) + ', -' + str(log0.replace(",","")) + ',' + '"' + str(sums) + '"' + ']'
            else:
                pointlatlong = ',[' + str(lat0.replace(",","")) + ',-' + str(log0.replace(",","")) + ',' + '"' + str(sums) + '"' + ']'
            count+=1
            #print(pointlatlong)
            crimesfinal.write(pointlatlong)
            coordinates_for_heatmap.append(pointlatlong)
        crimesfinal.write("]")
        return coordinates_for_heatmap


        # crime_a = []
        # crime_a.append('{ "type": "FeatureCollection", "features": [')
        # for i in r['crimes']:
        #     #{ "type": "FeatureCollection", "features": [{
        #     hello = '{ "type": "Feature", "geometry": { "type": "Point", "coordinates":'
        #     hall = hello.replace("'","")
        # #    print(hall)
        #     hello2 = str(i["Location"])
        #     variable = hello2.find("-")
        #     #print(variable)
        #     hllo = hello2[:variable].replace("(", "")
        #     hllo2 = hllo.replace(",", "")
        #     hi = hello2[variable:].replace(")", "")
        #     #print(hllo)
        #     sup = "[" + hi + ", " + hllo2 + "]"
        #     print(sup)
        #     hello3 = hall + sup.replace("'{"," {") + "}}"
        #     #print(hello3)
        #     crime_a.append(hello3)
        #     #print(i["Location"])
        # crime_a.append("]};")
        # #print(crime_a)
        # hello = open('/Users/Jesus/Desktop/project3/project3/fixedcrimes.txt')
        # responsetext.write(str(crime_a))
        # crimesfinal = open("crimes.txt", "w")
        # text = ""
        #
        # for i in hello.readline():
        #     #print(i)
        #     text = i
        #     if text == "'":
        #         text  = text.replace("'", "")
        #         crimesfinal.write(str(text))
        #     else:
        #         crimesfinal.write(str(text))
        #
        #
        # return crime_a

    #    s = json.dumps(r, sort_keys= True, indent = 2)
        #print(s)
    #    repo.dropCollection("crimerate")
    #    repo.createCollection("crimerate")

    #    repo["lc546_jofranco.crimerate"].insert_many([r])
    #    repo["lc546_jofranco.crimerate"].metadata({'complete':True})
    #    print(repo["lc546_jofranco.crimerate"].metadata())
    #    repo.logout()
    #    endTime = datetime.datetime.now()
    #    return {"start":startTime, "end":endTime}

    @staticmethod
    def provenance():
        pass

crimerate.execute()
