def make_readable(seconds):
    ss = seconds % 60
    ss_string = "{:02d}".format(ss)
    
    mm = int(((seconds - ss) / 60) % 60)
    mm_string = "{:02d}".format(mm)

    hh = int(((seconds - ss - (60 * mm)) / 60) / 60)
    hh_string = "{:02}".format(hh)

    time = [hh_string, mm_string, ss_string]

    return ":".join(time)
    
# Test.assert_equals(make_readable(0), "00:00:00")
# Test.assert_equals(make_readable(5), "00:00:05")
# Test.assert_equals(make_readable(60), "00:01:00")
# Test.assert_equals(make_readable(86399), "23:59:59")
# Test.assert_equals(make_readable(359999), "99:59:59")