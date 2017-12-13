function onLinkedInLoad() {
        IN.Event.on(IN, "auth", getProfileData);
}
// Use the API call wrapper to request the member's profile data
function getProfileData() {
    IN.API.Profile("me").fields("id", "first-name", "last-name", "headline", "location", "picture-url", "public-profile-url", "email-address").result(displayProfileData).error(onError);
}

// Handle the successful return from the API call
function displayProfileData(data){
    var user = data.values[0];
    console.log(data);
    IN.API.Raw('companies?format=json&is-company-admin=true')
        .method('GET')
        .result(getProfileCompanyData);
};


function shareContent() {
    
// Build the JSON payload containing the content to be shared
var payload = { 
    "comment": "Check out developer.linkedin.com! http://linkd.in/1FC2PyG", 
    "visibility": { 
    "code": "anyone"
    } 
};

var cpnyID = 13601373;

IN.API.Raw("/companies/" + cpnyID + "/shares?format=json")
    .method("POST")
    .body(JSON.stringify(payload))
    .result(onSuccess)
    .error(onError);
  }
 
getProfileCompanyData = (data)=>{
    comp = data.values
    company_id = comp[0].id
    IN.API.Raw('/companies/'+comp[0].id+':(id,name,company-type,website-url,logo-url,specialties,locations,description)?format=json')
        .method('GET')
        .result(postProfileCompanyData)

}

openProfile= (id)=>{
    alert('open');
    window.open('/fitur-2/'+id+'/', '_self')
}

postProfileCompanyData=(data)=>{
    console.log(data)
    id = data.id
    name = data.name
    com_type = data.companyType.name
    website = data.websiteUrl
    logo_url = data.logoUrl
    desc = data.description
    specialties = data.specialties
    address = data.locations
    $.ajax({
        method: "POST",
        url: '/fitur-2/add-company/',
        data: {
            id: id,
            name:name,
            com_type:com_type,
            website:website,
            logo_url:logo_url,
            desc:desc,
            specialties:specialties,
            address:address,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
        success: function (id){
            openProfile(id)
        },
        error: function (error){
            console.log(error)
        }

    })
}

// Handle an error response from the API call
function onError(error) {
    console.log(error);
}