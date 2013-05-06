/**
 * Created with PyCharm.
 * User: Henk
 * Date: 5/3/13
 * Time: 12:17 PM
 * To change this template use File | Settings | File Templates.
 */

/*

1.make distiction between using json as alternative to xml for importing and exporting LOCStructures
2. using json in an API to transfer data as javascript object for to be easy consumable by javascript frameworks

in the latter case json should match as closely as possible to an object in javascript

*/

var titleEn = locstructure.titles.en;
var titleFr = locstructure.titles.fr;

var sample_titles =
    [
        {
            "?":"Wine grower (m/f)" // no language code
        },
        {
            "en": "Wine grower (m/f)"
        },
        {
            "de": "Winzer/Winzerin"
        },
        {
            "nl": "Wijnmaker"
        },
        {
            "fr": "Vigneron"
        }
    ]


//instead of

var  loc_titles = [
        {"content": "Wine grower (m/f)"},
        {
            "language": "de",
            "content": "Winzer/Winzerin"
        }
    ]

var titleDefault = locstructure.titles.content;
//var titleDe = locstructure.titles.
//var titleFr = locstructure.?