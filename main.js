links = document.querySelectorAll('a')

str = ''

for(let i = 0; i < links.length; i++){
	if(links[i].classList.contains('ytd-playlist-panel-video-renderer')){
        str += '"' + links[i].href + '" '
	}
}

console.log(str)
