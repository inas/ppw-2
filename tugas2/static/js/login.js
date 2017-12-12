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
    /*var id = user.id;
    console.log(id);
    IN.API.Raw("/companies?format=json&is-company-admin=true").method("GET").result(
        function(response){
            console.log(response.values[0].id)
            $.ajax({
                method :"POST",
                url: "fitur-1/add-session",
                data: {
                    name: user.firstName + " " + user.lastName,
                    id : id,
                    companyID : response.values[0].id,
                    csrfmiddlewaretoken : '{{csrf_token}}'
                },
                success : function(){}
                error : function(){}
            });
        });*/
    document.getElementById("picture").innerHTML = '<img src="'+user.pictureUrl+'" />';
    document.getElementById("name").innerHTML = user.firstName+' '+user.lastName;
    document.getElementById("intro").innerHTML = user.headline;
    document.getElementById("email").innerHTML = user.emailAddress;
    document.getElementById("location").innerHTML = user.location.name;
    document.getElementById("link").innerHTML = '<a href="'+user.publicProfileUrl+'" target="_blank">Visit profile</a>';
    document.getElementById('profileData').style.display = 'block';
    document.getElementById('loginPage').style.display='none';
    document.body.style.backgroundColor='#fafafa';
    document.body.style.marginTop="70px";
    $('.navigation-list').append('<li id="#logoutBt"><a onclick="logout()">Log out</a></li>')

}

// Handle an error response from the API call
function onError(error) {
    console.log(error);
}

// Destroy the session of linkedin
function logout(){
    IN.User.logout(removeProfileData);}

// Remove profile data from page
function removeProfileData(){
    document.getElementById('profileData').remove();
    document.body.style.marginTop="0px";
    document.getElementById('loginPage').style.display='block';
    document.getElementsByClass('login_pages')[0].style.marginTop="40px";
}