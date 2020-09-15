const Nightmare = require('nightmare')

function showHelp() {
    console.log(`
        \rUsage: node sleepynightnight.js [email] [password] [...OPTION]

        \rAvailable OPTION:
        \r  --help    show this help
        \r  --debug   open up devtools for debugging purpose
    `)
}

if (process.argv.length < 4){
    showHelp()
    return
}

var args = process.argv.slice(2);

if (args.includes('--help')) {
    showHelp()
    return
}

var allOption = { 
    waitTimeout: 15000,
    typeInterval: 20,
}

if (args.includes('--debug')) {
    allOption.openDevTools = {
        mode: 'detach'
    };
    allOption.show = true;
}

const nightmare = Nightmare(allOption)
const username = args[0]
const password = args[1]

nightmare
    .goto('https://lms.telkomuniversity.ac.id/auth/oidc')
    .wait(5000)
    .type('#i0116', username)
    .click('#idSIButton9')
    .wait('#i0118')
    .type('#i0118', password)
    .wait(1000)
    .click('#idSIButton9')
    .wait('#KmsiDescription')
    .click('#idBtn_Back')
    .wait(5000)
    .wait('#page-my-index')
    .cookies.get('MoodleSession')
    .end()
    .then(cookie => {
        console.log("Cookie: " + JSON.stringify(cookie))
    })
    .catch(_ => {
      console.log('[!] Login failed')
    })
