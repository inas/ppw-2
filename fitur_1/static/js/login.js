// Use the API call wrapper to request the member's profile data
function getProfileData() {
    IN.API.Profile("me").fields("id", "first-name", "last-name", "headline", "location", "picture-url", "public-profile-url", "email-address").result(displayProfileData).error(onError);
}

// Handle the successful return from the API call
function displayProfileData(data){
    var user = data.values[0];
    $('#all').html(
      '<div id="profileData" style="display: none;">'+
        '<p><a href="javascript:void(0);" onclick="logout()">Logout</a></p>'+
      '<div id="picture"></div>'+
      '<div class="info">'+
        '<p id="name"></p>'+
        '<p id="intro"></p>'+
        '<p id="email"></p>'+
        '<p id="location"></p>'+
        '<p id="link"></p>'+
      '</div>'+
      '</div>')
    document.getElementById("picture").innerHTML = '<img src="'+user.pictureUrl+'" />';
    document.getElementById("name").innerHTML = user.firstName+' '+user.lastName;
    document.getElementById("intro").innerHTML = user.headline;
    document.getElementById("email").innerHTML = user.emailAddress;
    document.getElementById("location").innerHTML = user.location.name;
    document.getElementById("link").innerHTML = '<a href="'+user.publicProfileUrl+'" target="_blank">Visit profile</a>';
    document.getElementById('profileData').style.display = 'block';
    document.body.style.backgroundColor='#fafafa';
    document.body.style.marginTop="70px";
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
    window.location.replace('/fitur-1')
    }