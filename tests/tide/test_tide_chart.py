from tidal_pi.tide.tide_chart import TideChart
from tide.tide_chart_fixtrue import get_tides_fixture
from tide.tide_chart_fixtrue_2 import get_tides_fixture_2
from tide.tide_chart_fixtrue_3 import get_tides_fixture_3


def test_get_tide_state():
    tide_chart = TideChart(get_tides_fixture())
    tide_state = tide_chart.get_tide_state("2020-09-27 20:24")

    current_tide_level = tide_state.get_current_tide_level()
    assert current_tide_level.get_percent_of_high_tide() == 97.4

    previous_tide = tide_state.get_previous_tide()
    assert previous_tide.get_date() == "2020-09-27"
    assert previous_tide.get_time() == "20:14"
    assert previous_tide.get_type() == "H"
    assert previous_tide.get_height() == "7.222"

    next_tide = tide_state.get_next_tide()
    assert next_tide.get_date() == "2020-09-28"
    assert next_tide.get_time() == "02:38"
    assert next_tide.get_type() == "L"
    assert next_tide.get_height() == "0.880"

    next_high_tide = tide_state.get_next_high_tide()
    assert next_high_tide.get_date() == "2020-09-28"
    assert next_high_tide.get_time() == "08:28"
    assert next_high_tide.get_type() == "H"
    assert next_high_tide.get_height() == "6.558"

    next_low_tide = tide_state.get_next_low_tide()
    assert next_low_tide.get_date() == "2020-09-28"
    assert next_low_tide.get_time() == "02:38"
    assert next_low_tide.get_type() == "L"
    assert next_low_tide.get_height() == "0.880"



def test_get_tide_state_span_day():
    tide_chart = TideChart(get_tides_fixture())
    tide_state = tide_chart.get_tide_state("2020-09-27 00:24")

    current_tide_level = tide_state.get_current_tide_level()
    assert current_tide_level.get_percent_of_high_tide() == 21.19

    previous_tide = tide_state.get_previous_tide()
    assert previous_tide.get_date() == "2020-09-26"
    assert previous_tide.get_time() == "19:19"
    assert previous_tide.get_type() == "H"
    assert previous_tide.get_height() == "7.208"

    next_tide = tide_state.get_next_tide()
    assert next_tide.get_date() == "2020-09-27"
    assert next_tide.get_time() == "01:46"
    assert next_tide.get_type() == "L"
    assert next_tide.get_height() == "0.969"

    next_high_tide = tide_state.get_next_high_tide()
    assert next_high_tide.get_date() == "2020-09-27"
    assert next_high_tide.get_time() == "07:33"
    assert next_high_tide.get_type() == "H"
    assert next_high_tide.get_height() == "6.393"

    next_low_tide = tide_state.get_next_low_tide()
    assert next_low_tide.get_date() == "2020-09-27"
    assert next_low_tide.get_time() == "01:46"
    assert next_low_tide.get_type() == "L"
    assert next_low_tide.get_height() == "0.969"


def test_get_tide_state_2():
    tide_chart = TideChart(get_tides_fixture_2())
    tide_state = tide_chart.get_tide_state("2020-10-04 00:09")

    current_tide_level = tide_state.get_current_tide_level()
    assert current_tide_level.get_percent_of_high_tide() == 97.73

    previous_tide = tide_state.get_previous_tide()
    assert previous_tide.get_date() == "2020-10-03"
    assert previous_tide.get_time() == "18:25"
    assert previous_tide.get_type() == "L"
    assert previous_tide.get_height() == "0.925"

    next_tide = tide_state.get_next_tide()
    assert next_tide.get_date() == "2020-10-04"
    assert next_tide.get_time() == "00:17"
    assert next_tide.get_type() == "H"
    assert next_tide.get_height() == "6.699"

    next_high_tide = tide_state.get_next_high_tide()
    assert next_high_tide.get_date() == "2020-10-04"
    assert next_high_tide.get_time() == "00:17"
    assert next_high_tide.get_type() == "H"
    assert next_high_tide.get_height() == "6.699"

    next_low_tide = tide_state.get_next_low_tide()
    assert next_low_tide.get_date() == "2020-10-04"
    assert next_low_tide.get_time() == "06:32"
    assert next_low_tide.get_type() == "L"
    assert next_low_tide.get_height() == "0.747"

def test_get_tide_state_3():
    tide_chart = TideChart(get_tides_fixture_3())
    tide_state = tide_chart.get_tide_state("2020-10-05 08:23")

    current_tide_level = tide_state.get_current_tide_level()
    assert current_tide_level.get_percent_of_high_tide() == 21.31
    assert current_tide_level.get_tide_type() == "L"

    previous_tide = tide_state.get_previous_tide()
    assert previous_tide.get_date() == "2020-10-05"
    assert previous_tide.get_time() == "07:05"
    assert previous_tide.get_type() == "L"
    assert previous_tide.get_height() == "0.900"

    next_tide = tide_state.get_next_tide()
    assert next_tide.get_date() == "2020-10-05"
    assert next_tide.get_time() == "13:11"
    assert next_tide.get_type() == "H"
    assert next_tide.get_height() == "7.057"

    next_high_tide = tide_state.get_next_high_tide()
    assert next_high_tide.get_date() == "2020-10-05"
    assert next_high_tide.get_time() == "13:11"
    assert next_high_tide.get_type() == "H"
    assert next_high_tide.get_height() == "7.057"

    next_low_tide = tide_state.get_next_low_tide()
    assert next_low_tide.get_date() == "2020-10-05"
    assert next_low_tide.get_time() == "19:38"
    assert next_low_tide.get_type() == "L"
    assert next_low_tide.get_height() == "1.289"