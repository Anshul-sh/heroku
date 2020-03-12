import json
import pandas as pd

from src.twitter.authentication.TwitterAPIAuthentication import TwitterAPIAuthentication
from src.twitter.search.search import Search
# FIXME: Same name as .py file in watson API!
from src.watson.tone_analysis.tone_analysis import ToneAnalysis
def main():
    """
    Demonstrate the process of data flow.
    :return:
    """
    # Get Data from twitter part.
    a = TwitterAPIAuthentication()
    api = a.get_authentication()
    s = Search()
    s.initialize(api, '@realdonaldtrump')
    r = s.search_a_tweet_and_its_replies()
    print(r[0])
    print(r[1])
    for t in r[1]:
        print(t.text)
    print('-----Twitter API Done-----')
    # Twitter part done.
    # Process the data(Very Sample)
    text = ''
    for t in r[1]:
        text += (t.text + '\n')
    # Process the data done
    # Tone Analysis
    Ta = ToneAnalysis()
    Ta.tone_analysis_by_str(text)
    result = Ta.get_tone_analysis_result()
    # Tone Analysis Done
    # Display result

    with open('Output/Output.json','w') as file_write:
        file_write.write(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
