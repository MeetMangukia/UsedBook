$( function() {
    var availableTags = [
       'Surat, Gujarat',
       'Ahamdabad, Gujarat',
       'Vadodara, Gujarat',
       'Gandhinagar, Gujarat',
       'jamnagar, Gujarat',
 
       'Pune, Maharashtra',
       'Nagpur, Maharashtra',
       'Nashik, Maharashtra',
       'Solapur, Maharashtra',
       'Jalgaon, Maharashtra',
 
       'Bengaluru, Karnataka',
       'Mysuru, Karnataka',
       'Belagavi, Karnataka',
       'Vijayapura, Karnataka',
       'Raichur, Karnataka',
 
       'Ludhiana, Punjab',
       'Amritsar, Punjab',
       'Jalandhar, Punjab',
       'Patiala, Punjab',
       'Bathinda, Punjab',
 
       'Jaipur, Rajasthan',
       'Jodhpur, Rajasthan',
       'Udaipur, Rajasthan',
       'Jaisalmer, Rajasthan',
       'Pushkar, Rajasthan',
    ];
    $( "#search_location" ).autocomplete({
      source: availableTags
    });
});