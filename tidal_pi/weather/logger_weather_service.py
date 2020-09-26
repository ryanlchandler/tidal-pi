import logging
import json


class LoggerWeatherService():

    def fetch_tide_forecast(self, begin_date, end_date):
        logging.info("fetching tide forecast for {} to {}".format(begin_date, end_date))
        resp_text = """
        { "predictions" : [{"t":"2020-09-23 03:31", "v":"6.838", "type":"H"},{"t":"2020-09-23 09:52", "v":"0.298", "type":"L"},{"t":"2020-09-23 16:12", "v":"7.620", "type":"H"},{"t":"2020-09-23 22:47", "v":"0.801", "type":"L"},{"t":"2020-09-24 04:28", "v":"6.549", "type":"H"},{"t":"2020-09-24 10:54", "v":"0.579", "type":"L"},{"t":"2020-09-24 17:14", "v":"7.394", "type":"H"},{"t":"2020-09-24 23:50", "v":"0.958", "type":"L"},{"t":"2020-09-25 05:29", "v":"6.361", "type":"H"},{"t":"2020-09-25 11:57", "v":"0.757", "type":"L"},{"t":"2020-09-25 18:18", "v":"7.252", "type":"H"},{"t":"2020-09-26 00:50", "v":"1.004", "type":"L"},{"t":"2020-09-26 06:33", "v":"6.312", "type":"H"},{"t":"2020-09-26 12:58", "v":"0.841", "type":"L"},{"t":"2020-09-26 19:19", "v":"7.208", "type":"H"},{"t":"2020-09-27 01:46", "v":"0.969", "type":"L"},{"t":"2020-09-27 07:33", "v":"6.393", "type":"H"},{"t":"2020-09-27 13:56", "v":"0.857", "type":"L"},{"t":"2020-09-27 20:14", "v":"7.222", "type":"H"},{"t":"2020-09-28 02:38", "v":"0.880", "type":"L"},{"t":"2020-09-28 08:28", "v":"6.558", "type":"H"},{"t":"2020-09-28 14:50", "v":"0.831", "type":"L"},{"t":"2020-09-28 21:02", "v":"7.243", "type":"H"},{"t":"2020-09-29 03:26", "v":"0.767", "type":"L"},{"t":"2020-09-29 09:16", "v":"6.750", "type":"H"},{"t":"2020-09-29 15:40", "v":"0.784", "type":"L"},{"t":"2020-09-29 21:46", "v":"7.232", "type":"H"},{"t":"2020-09-30 04:09", "v":"0.658", "type":"L"},{"t":"2020-09-30 10:00", "v":"6.929", "type":"H"},{"t":"2020-09-30 16:26", "v":"0.750", "type":"L"},{"t":"2020-09-30 22:26", "v":"7.174", "type":"H"}]}
        """
        return json.loads(resp_text)["predictions"]



