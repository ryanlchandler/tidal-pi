from tidal_pi.tide.tide import Tide

def get_tides_fixture_3():
  tides = {}
  for index in tides_dict:
    tides[index] = []
    for tide in tides_dict[index]:
      tides[index].append(Tide(tide["date"], tide["time"], tide["type"], tide["height"]))
  return tides


tides_dict = {
  "6": [
    {
      "date": "2020-10-04",
      "time": "00:17",
      "type": "H",
      "height": "6.699"
    },
    {
      "date": "2020-10-04",
      "time": "06:32",
      "type": "L",
      "height": "0.747"
    },
    {
      "date": "2020-10-04",
      "time": "12:34",
      "type": "H",
      "height": "7.134"
    },
    {
      "date": "2020-10-04",
      "time": "19:01",
      "type": "L",
      "height": "1.092"
    },
    {
      "date": "2020-10-11",
      "time": "05:32",
      "type": "H",
      "height": "5.999"
    },
    {
      "date": "2020-10-11",
      "time": "12:02",
      "type": "L",
      "height": "1.153"
    },
    {
      "date": "2020-10-11",
      "time": "18:09",
      "type": "H",
      "height": "7.015"
    }
  ],
  "0": [
    {
      "date": "2020-10-05",
      "time": "00:54",
      "type": "H",
      "height": "6.481"
    },
    {
      "date": "2020-10-05",
      "time": "07:05",
      "type": "L",
      "height": "0.900"
    },
    {
      "date": "2020-10-05",
      "time": "13:11",
      "type": "H",
      "height": "7.057"
    },
    {
      "date": "2020-10-05",
      "time": "19:38",
      "type": "L",
      "height": "1.289"
    }
  ],
  "1": [
    {
      "date": "2020-10-06",
      "time": "01:31",
      "type": "H",
      "height": "6.266"
    },
    {
      "date": "2020-10-06",
      "time": "07:40",
      "type": "L",
      "height": "1.065"
    },
    {
      "date": "2020-10-06",
      "time": "13:49",
      "type": "H",
      "height": "6.962"
    },
    {
      "date": "2020-10-06",
      "time": "20:18",
      "type": "L",
      "height": "1.489"
    }
  ],
  "2": [
    {
      "date": "2020-10-07",
      "time": "02:10",
      "type": "H",
      "height": "6.078"
    },
    {
      "date": "2020-10-07",
      "time": "08:18",
      "type": "L",
      "height": "1.218"
    },
    {
      "date": "2020-10-07",
      "time": "14:30",
      "type": "H",
      "height": "6.872"
    },
    {
      "date": "2020-10-07",
      "time": "21:03",
      "type": "L",
      "height": "1.659"
    }
  ],
  "3": [
    {
      "date": "2020-10-08",
      "time": "02:52",
      "type": "H",
      "height": "5.938"
    },
    {
      "date": "2020-10-08",
      "time": "09:03",
      "type": "L",
      "height": "1.337"
    },
    {
      "date": "2020-10-08",
      "time": "15:16",
      "type": "H",
      "height": "6.811"
    },
    {
      "date": "2020-10-08",
      "time": "21:56",
      "type": "L",
      "height": "1.758"
    }
  ],
  "4": [
    {
      "date": "2020-10-09",
      "time": "03:38",
      "type": "H",
      "height": "5.859"
    },
    {
      "date": "2020-10-09",
      "time": "09:57",
      "type": "L",
      "height": "1.389"
    },
    {
      "date": "2020-10-09",
      "time": "16:08",
      "type": "H",
      "height": "6.798"
    },
    {
      "date": "2020-10-09",
      "time": "22:54",
      "type": "L",
      "height": "1.738"
    }
  ],
  "5": [
    {
      "date": "2020-10-10",
      "time": "04:31",
      "type": "H",
      "height": "5.867"
    },
    {
      "date": "2020-10-10",
      "time": "10:58",
      "type": "L",
      "height": "1.335"
    },
    {
      "date": "2020-10-10",
      "time": "17:06",
      "type": "H",
      "height": "6.857"
    },
    {
      "date": "2020-10-10",
      "time": "23:53",
      "type": "L",
      "height": "1.573"
    }
  ]
}