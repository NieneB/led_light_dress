function SendSignal(Signal) { 
	xhttp = new XMLHttpRequest();
	xhttp.open("GET", "?Signal=" + Signal, false);
	xhttp.send();
}


