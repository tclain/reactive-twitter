from web.code.engine.analysis import Language



class TweetAnalyser():
    '''
    Analyse Language and word/chars statistics
    return a hash :
    {
        "lang" : "english",
        "word_count" : "12",
        "lexical_diversity" : 0.52
    }
    '''
    @staticmethod
    def stats(tweet, channel, callback):
        inner_text = tweet["text"]
        guess = Language.guess(inner_text)
        #processed object
        processed = {"tweet" : Language.guess}
        if guess == "swedish" : #false positives
            callback(processed)
        else :
            processed["lang"] = guess
            callback(processed)
        return True