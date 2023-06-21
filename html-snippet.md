{
	// Place your snippets for html here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"Django Template Block": {
		"prefix": "dtb",
		"body": [
		"{% block $1 %}",
		"",
		"{% endblock $1 %}"
		],
		"description": "Django Template Block"
		},
		"Django Template Extends": {
		"prefix": "dte",
		"body": [
		"{% extends '$1.html' %}"
		],
		"description": "Django Template Extends"
		},
		"Django Template Tag": {
		"prefix": "dtt",
		"body": [
		"{% $1 %}"
		],
		"description": "Django Template Tag"
		},
		"django template child": {
		"prefix": "dtc",
		"body": [
		"{% extends '$1.html' %}",
		"",
		"{% block content %}",
		"  <h2>$2 coming soon</h2>",
		"{% endblock content %}"
		],
		"description": "django template child"
		},
		"Django Template Form": {
		"prefix": "dtf",
		"body": [
		"<form action=\"\" method=\"POST\">",
		"  {% csrf_token %}",
		"  {{ form.as_p }}",
		"  <input type=\"submit\" value=\"$1\">",
		"</form>"
		],
		"description": "Django Template Form"
		}
}