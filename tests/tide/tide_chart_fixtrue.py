from tidal_pi.tide.tide import Tide

def get_tides_fixture():
  tides = {}
  for index in tides_dict:
    tides[index] = []
    for tide in tides_dict[index]:
      tides[index].append(Tide(tide["date"], tide["time"], tide["type"], tide["height"]))
  return tides


tides_dict = {
      "2": [
        {
          "date": "2020-09-23",
          "time": "03:31",
          "type": "H",
          "height": "6.838"
        },
        {
          "date": "2020-09-23",
          "time": "09:52",
          "type": "L",
          "height": "0.298"
        },
        {
          "date": "2020-09-23",
          "time": "16:12",
          "type": "H",
          "height": "7.620"
        },
        {
          "date": "2020-09-23",
          "time": "22:47",
          "type": "L",
          "height": "0.801"
        },
        {
          "date": "2020-09-30",
          "time": "04:09",
          "type": "L",
          "height": "0.658"
        },
        {
          "date": "2020-09-30",
          "time": "10:00",
          "type": "H",
          "height": "6.929"
        },
        {
          "date": "2020-09-30",
          "time": "16:26",
          "type": "L",
          "height": "0.750"
        },
        {
          "date": "2020-09-30",
          "time": "22:26",
          "type": "H",
          "height": "7.174"
        }
      ],
      "3": [
        {
          "date": "2020-09-24",
          "time": "04:28",
          "type": "H",
          "height": "6.549"
        },
        {
          "date": "2020-09-24",
          "time": "10:54",
          "type": "L",
          "height": "0.579"
        },
        {
          "date": "2020-09-24",
          "time": "17:14",
          "type": "H",
          "height": "7.394"
        },
        {
          "date": "2020-09-24",
          "time": "23:50",
          "type": "L",
          "height": "0.958"
        }
      ],
      "4": [
        {
          "date": "2020-09-25",
          "time": "05:29",
          "type": "H",
          "height": "6.361"
        },
        {
          "date": "2020-09-25",
          "time": "11:57",
          "type": "L",
          "height": "0.757"
        },
        {
          "date": "2020-09-25",
          "time": "18:18",
          "type": "H",
          "height": "7.252"
        }
      ],
      "5": [
        {
          "date": "2020-09-26",
          "time": "00:50",
          "type": "L",
          "height": "1.004"
        },
        {
          "date": "2020-09-26",
          "time": "06:33",
          "type": "H",
          "height": "6.312"
        },
        {
          "date": "2020-09-26",
          "time": "12:58",
          "type": "L",
          "height": "0.841"
        },
        {
          "date": "2020-09-26",
          "time": "19:19",
          "type": "H",
          "height": "7.208"
        }
      ],
      "6": [
        {
          "date": "2020-09-27",
          "time": "01:46",
          "type": "L",
          "height": "0.969"
        },
        {
          "date": "2020-09-27",
          "time": "07:33",
          "type": "H",
          "height": "6.393"
        },
        {
          "date": "2020-09-27",
          "time": "13:56",
          "type": "L",
          "height": "0.857"
        },
        {
          "date": "2020-09-27",
          "time": "20:14",
          "type": "H",
          "height": "7.222"
        }
      ],
      "0": [
        {
          "date": "2020-09-28",
          "time": "02:38",
          "type": "L",
          "height": "0.880"
        },
        {
          "date": "2020-09-28",
          "time": "08:28",
          "type": "H",
          "height": "6.558"
        },
        {
          "date": "2020-09-28",
          "time": "14:50",
          "type": "L",
          "height": "0.831"
        },
        {
          "date": "2020-09-28",
          "time": "21:02",
          "type": "H",
          "height": "7.243"
        }
      ],
      "1": [
        {
          "date": "2020-09-29",
          "time": "03:26",
          "type": "L",
          "height": "0.767"
        },
        {
          "date": "2020-09-29",
          "time": "09:16",
          "type": "H",
          "height": "6.750"
        },
        {
          "date": "2020-09-29",
          "time": "15:40",
          "type": "L",
          "height": "0.784"
        },
        {
          "date": "2020-09-29",
          "time": "21:46",
          "type": "H",
          "height": "7.232"
        }
      ]
    }