#!/usr/bin/env python3


def acronyms(s):
    result=[]
    # for word in s.split(" "):
    #     word_clean=word.strip(".,()")
    #     if len(word_clean)>1 and word_clean.isupper():
    #         result.append(word_clean)
        # s = s.replace(",", "")
    result = [word.strip(".,()") for word in s.split(" ") if len(word.strip(".,()")) > 1 and word.strip(".,()").isupper()]

    return result

def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
