filenames = ['C:/Users/maol.KYIV/Downloads/tweets.1431014541083.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1433116992116.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1435710129458.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1438387271627.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1441066967918.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1443092418166.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1443100087132.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1443658017814.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1446336487602.dat.tmp'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1447407788557.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1451400591729.dat'
    , 'C:/Users/maol.KYIV/Downloads/tweets.1448928361771.dat.tmp']

with open('C:/Users/maol.KYIV/Downloads/tweets.2015.txt', 'w', encoding='utf-8') as outfile:
    for fname in filenames:
        with open(fname, encoding="utf8") as infile:
            for line in infile:
                outfile.write(line)
            outfile.write('\n')
