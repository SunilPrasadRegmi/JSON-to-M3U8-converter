import json

with open('channels.json') as f:
    data = json.load(f)

with open('playlist.m3u8', 'w') as f:
    f.write('#EXTM3U\n')

    for channel in data:
        name = channel['channel_name']
        chid = channel['id']
        chno = channel['channel_number']
        category = channel['category']
        logo = channel['logo']
        url = channel['url']

        f.write(f'#EXTINF:-1 tvg-id="{chid}" tvg-chno="{chno}" group-title="{category}" tvg-logo="{logo}", {name}\n{url}\n')

print("File saved as playlist.m3u8")