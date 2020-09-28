from tidal_pi.tide.tide_chart import TideChart
from tide.tide_chart_fixtrue import get_tides_fixture


def test_get_tide_state():
    tide_chart = TideChart(get_tides_fixture())
    tide_state = tide_chart.get_tide_state("2020-09-27 20:24")
    previous_tide = tide_state.get_previous_tide()

    assert previous_tide.get_date() == "2020-09-27"
    assert previous_tide.get_time() == "20:14"
    assert previous_tide.get_type() == "H"
    assert previous_tide.get_height() == "7.222"

def test_get_tide_state_span_day():
    tide_chart = TideChart(get_tides_fixture())
    tide_state = tide_chart.get_tide_state("2020-09-27 00:24")
    previous_tide = tide_state.get_previous_tide()

    assert previous_tide.get_date() == "2020-09-26"
    assert previous_tide.get_time() == "19:19"
    assert previous_tide.get_type() == "H"
    assert previous_tide.get_height() == "7.208"