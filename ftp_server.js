const ftpd = require('ftpd');
const PORT = 21;
const USERS = [
    { username: 'USERNAME', password: 'PASSWORD', directory: 'PATH' },
];

const server = new ftpd.FtpServer('0.0.0.0', {
    getInitialCwd: function () {
        return '/';
    },
    getRoot: function (connection) {
        const user = USERS.find(user => user.username === connection.username);

        return user.directory;
    },
    pasvPortRangeStart: 1024,
    pasvPortRangeEnd: 65535,
    useWriteFile: false,
    useReadFile: false
});

server.on('client:connected', function (connection) {
    var username = null;

    connection.on('command:user', function (user, success, failure) {
        if (user) {
            username = user;
            success();
        } else {
            failure();
        }
    });

    connection.on('command:pass', function (pass, success, failure) {
        const user = USERS.find(user => user.username === username && user.password === pass);

        if (pass && user) {
            success(username);
        } else {
            failure();
        }
    });
});

server.debugging = -1;

server.listen(PORT);
