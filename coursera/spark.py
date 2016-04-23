#fileA = sc.textFile("/data/social/vkontakte/join1_FileA.txt")
#fileB = sc.textFile("/data/social/vkontakte/join1_FileB.txt")
show_views_file = sc.textFile("/data/social/vkontakte/join2_gennum?.txt")
show_channel_file = sc.textFile("/data/social/vkontakte/join2_genchan?.txt")
line = "able,991"
#word = line(lambda  x: (x.split(",")[0], x))
word = line.split(',')[0]
print(word)

def split_fileA(line):
    word = line.split(',')[0]
    count = line.split(',')[1]
    return (word, count)

def split_fileB(line):
    date, word_count  = (x for x in line.split())
    word, count_string  = (x for x in word_count.split(','))
    return (word, date + " " + count_string)

def split_show_views(line):
    show = line.split(',')[0]
    views = int(line.split(',')[1])
    return (show, views)

def split_show_channel(line):
    show, channel  = (x for x in line.split(','))
    return (show, channel)

def extract_channel_views(show_views_channel):
    chanel_views = show_views_channel[1]
    channel = chanel_views[0]
    views = chanel_views[1]
    return (channel, views)

def sum_of_views(a, b):
    some_result = a + b
    return some_result

show_views = show_views_file.flatMap(slit_show_views)
show_channel = show_channel_file.map(split_show_channel)

joined_dataset = show_channel.join(show_views)

channel_views = joined_dataset.map(extract_channel_views)

#.reduceByKey(lambda a, b: a + b)

channel_views.reduceByKey(sum_of_views).collect()