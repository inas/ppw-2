function onLinkedInLoad() {
    IN.Event.on(IN, "auth", getProfileData);
}
    
// Use the API call wrapper to request the member's profile data
function getProfileData() {
    IN.API.Profile("me").fields("id", "first-name", "last-name", "headline", "location", "picture-url", "public-profile-url", "email-address")
        .result(displayProfileData)
        .error(onError);
}

// Handle the successful return from the API call
function displayProfileData(data){
    var user = data.values[0];
    
    IN.API.Raw('companies?format=json&is-company-admin=true')
        .method('GET')
        .result(getProfileCompanyData);
}


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
    IN.API.Raw('companies/'+comp[0].id+':(id,name,email-domains,company-type,industries,twitter-id,website-url,logo-url,employee-count-range,specialties,locations,description,founded-year,num-followers)?format=json')
        .method('GET')
        .result(postProfileCompanyData)

}

openProfile= (id)=>{
    window.open('/fitur-2/'+id+'/', '_self')
}

postProfileCompanyData=(data)=>{
    console.log(JSON.stringify(data))
    id = data.id
    $.ajax({
        method: "POST",
        url: '/fitur-2/add-company/',
        data: data,
        dataType: 'json',
        id:id,
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
        success: function (id){
            openProfile(this.id)
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

// Destroy the session of linkedin
function logout(){
    IN.User.logout(removeProfileData);
    // document.location.reload();
}

// Remove profile data from page
function removeProfileData(){
    document.getElementById('profileData').remove();
}   