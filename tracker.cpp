#include <iostream>
#include <libphonenumber/phonenumberutil.h>
#include <libphonenumber/geocoder/geocodingphonemetadata.h>
#include <opencage/geocoder.h>

using namespace std;
using namespace phonenumbers;
using namespace opencage;

// Replace 'YOUR_API_KEY' with your actual API key from OpenCage Geocoder
const string API_KEY = "aae2ea08ff4a48839796c84462c1081a";

// Function to get location description for a phone number
string getLocation(const string& phone_number) {
    PhoneNumberUtil phone_util;
    PhoneNumber parsed_number;
    phone_util.Parse(phone_number, "", &parsed_number);
    string region_code = phone_util.GetRegionCodeForNumber(parsed_number);
    string location;
    GeocodingPhoneMetadata metadata(region_code);
    metadata.GetDescriptionForNumber(parsed_number, "en", &location);
    return location;
}

// Function to get coordinates using OpenCage Geocoder API
pair<double, double> getCoordinates(const string& location) {
    OpencageGeocoder geocoder(API_KEY);
    GeocoderResponse response = geocoder.geocode(location);
    if (!response.results.empty()) {
        double lat = response.results[0]["geometry"]["lat"].asDouble();
        double lng = response.results[0]["geometry"]["lng"].asDouble();
        return make_pair(lat, lng);
    }
    return make_pair(0.0, 0.0); // Default coordinates if not found
}

int main() {
    string phone_number;
    cout << "Enter the phone number: ";
    cin >> phone_number;

    string location = getLocation(phone_number);
    if (!location.empty()) {
        pair<double, double> coordinates = getCoordinates(location);
        double lat = coordinates.first;
        double lng = coordinates.second;
        if (lat != 0.0 && lng != 0.0) {
            cout << "Latitude: " << lat << endl;
            cout << "Longitude: " << lng << endl;
            // You can add code to create a map or perform other operations here
        } else {
            cout << "Failed to retrieve coordinates." << endl;
        }
    } else {
        cout << "Failed to retrieve location information." << endl;
    }

    return 0;
}
