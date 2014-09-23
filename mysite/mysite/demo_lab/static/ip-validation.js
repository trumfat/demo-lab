function ValidateIP(inputText)  {  
	var ipformat = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;  

	if(inputText.value.match(ipformat)) {  
		document.IP.ip.focus();  
		return true;  
	} else {  
		alert("You have entered an invalid IP address!");  
		document.IP.ip.focus();
		return false;  
	}  
}
