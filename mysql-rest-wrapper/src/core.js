const Config = require('./config.json')
const mysql = require('mysql');
const express = require('express');
const morgan = require('morgan')
const http = express();

http.use(express.json());
http.use(morgan('combined'))

for (const name in Config.servers) {
	const config = Config.servers[name];
	const _temp = mysql.createConnection({
		host: config.host,
		port: config.port,
		user: config.user,
		password: config.password,
		database: config.database
	});

	_temp.connect(function(err) {
		if (err) throw err;
		console.log(name + ' connected!');
		http.post('/' + name, (request, response) => {
			if (config.key == request.body.key) {
				_temp.query(request.body.query, function(error, result, fields) {
					response.send({
						'result': (result == undefined ? null : result),
						'fields': (fields == undefined ? null : fields),
						'error': (error == undefined ? null : error)
					});
				});
			} else {
				response.status(403).send();
			}
		});
		if (config.keepAlive != undefined && config.keepAlive > 0) {
			setInterval(function() {
				_temp.query('SELECT 1;', function(error) {
					if (error != null) {
						console.log(name + ' got an error while keeping alive!');
						console.log(error);
					}
				});
			}, config.keepAlive);
		}
	});
}

http.listen(Config.port, () => {
	console.log('Server listening!');
});