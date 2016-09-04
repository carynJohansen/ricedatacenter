/////////////////////////////
////    server side     ////
///////////////////////////

// Environment //

//dependencies
var express = require('express')
var app = express()
var http = require('http')
var path = require('path')
var request = require('request');
var bodyParser = require('body-parser')
var jade = require('jade')
var child = require('child_process')
var _ = require('underscore')
var json2csv = require('json2csv')
var fs = require('fs')

//Database connection
//var sqlite3 = require('sqlite3').verbose()
//var db = new sqlite3.Database('/Users/caryn/Dropbox/Project_jsLearn/simple_genes/michael.db')

//port
app.set('port', (process.env.PORT || 5000))

app.use(express.static('public'));
console.log(__dirname)

//set views
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');

//body parser
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

//app.use(express.logger('dev'))

// Methods //

app.get('/', function (request, response) {
    response.render('home', {
    	title:'Home'
    })
}) //close get /

app.get('/home', function (request, response) {
	response.render('home', {
		title: 'Gene Search Home'
	})
}) // close get home

app.post('/genesearch', function (request, response) {
	console.log('you made it to post genesearch!')
	response.render('genesearch', {
		title: 'Gene Search'
	})
})

app.get('/genesearch', function (request, response) {
	response.render('genesearch', {
		title: 'Gene Search'
	})
})

app.get('/searching', function (request, response) {
	//response.send('oh hi')
	var geneval = request.query.geneInput //this is for the ajax .get
	console.log("this is in the server", geneval)
	function show() {
		var geneval = request.query.geneInput
		console.log('geneval in show():', geneval)
		gene_vcf_search(geneval).then(function (geneJSON) {
			//console.log(geneJSON)
			response.send( {data : geneJSON, gene : geneval} )
		}) // close promise
	} //close show
	function gene_vcf_search (gene) {
		return new Promise( function (fulfill, reject) {
			console.log("you are in gene_vcf_search and this is the gene:", gene)
			var python = child.spawn('python', [__dirname + '/public/python/fetch_genome_information.py', gene])
			var data = ''
			python.stdout.on('data', function (chunk) {
				data += chunk
			}) //close stdout
			python.stderr.on('data', function (data) {
				console.log('python err: ' + data)
				response.end('python error in allele counts!' + data)
			}) //close stderr
			python.stdout.on('end', function() {
				fulfill(data)
			})
		}) // close promise
	} // close gene_vcf_search
	show()
}) // close searching

app.get('/downloadRegionVCF', function (request, response) {
	console.log("you clicked!")
	console.log(__dirname)
	function return_vcf() {
		var geneval = request.query.geneInput
		create_vcf(geneval).then(function() {
			response.send()
		});
	}; //close return_vcf()
	function create_vcf(gene) {
		console.log(gene)
		return new Promise( function (fulfill, reject) {
			var python = child.spawn('python', [__dirname + '/public/python/write_region_vcf.py', gene])
			var data = ''
			python.stdout.on('data', function (chunk) {
				data += chunk
			}) //close stdout
			python.stderr.on('data', function (data) {
				console.log('python err: ' + data)
				response.end('python error in allele counts!' + data)
			}) //close stderr
			python.stdout.on('end', function() {
				fulfill(data)
			})
		}) // close Promise
	} // close create_vcf function
	return_vcf()
}) // close downlosRegionVCF

app.get('/network', function (request, response) {
	response.render('network', {
		title: 'Search Interaction Network'
	})
}) //close networksearch

app.get('/createquery', function (request, response) {
	
	function return_query() {
		var queryJSON = request.query.inputJSON
		//console.log(queryJSON)
		create_query(queryJSON).then(function (queryStm) {
			response.send(queryStm)
		}) // close promise
	} // close return query

	function create_query ( jsonInfo ) {
		return new Promise( function (fulfill, reject) {
			var python = child.spawn('python', [__dirname + '/public/python/create_query.py', jsonInfo ])
			var data = ''
			python.stdout.on('data', function (chunk) {
				data += chunk
			}) //close stdout
			python.stderr.on('data', function (data) {
				console.log('python err: ' + data)
				response.end('python error in allele counts!' + data)
			}) //close stderr
			python.stdout.on('end', function() {
				fulfill(data)
			})
		}) // close new Promise
	} // close create_query
	return_query()
}) //close createquery

app.get('/querying', function (request, response) {
	function show () {
		testQuery().then(function (queryJSON) {
			console.log("in the show() step of querying!")
			response.send(queryJSON)
		})
	}
	function testQuery () {
		return new Promise( function (fulfill, reject) {
			var inquery = request.query.textQuery
			//console.log("and here we query the network in python...", inquery)
			var python = child.spawn('python', [__dirname + '/public/python/network_query.py', inquery])
			var data = ''
			python.stdout.on('data', function (chunk) {
				data += chunk
			}) //close stdout
			python.stderr.on('data', function (data) {
				console.log('python error:', data)
			})
			python.stdout.on('end', function() {
				fulfill(data)
			})
		}) //close new promise
	} // close testQuery function
	show()
})

app.get('/networkVis', function (request, response) {
	var net_input = request.query.netInput
	console.log("you're in networkVis:", net_input)
	response.json(net_input)
})

app.post('/categorysearch', function (request, response) {
	response.render('catsearch')
})

app.get('/categorysearch', function (request, response) {
	response.render('catsearch')
})

app.use('/download', function (request, response) {
	console.log("you made it to download!!")
	function dwnld() {
		var geneval = request.query.geneInput
		create_vcf(geneval).then(function (regionVCF) {
			response.download(queryStm)
		}) // close promise
	}
	
	function create_vcf(gene) {
		console.log(gene)
		return new Promise( function (fulfill, reject) {
			var python = child.spawn('python', [__dirname + '/public/python/write_region_vcf.py', gene])
			var data = ''
			python.stdout.on('data', function (chunk) {
				data += chunk
			}) //close stdout
			python.stderr.on('data', function (data) {
				console.log('python err: ' + data)
				response.end('python error in allele counts!' + data)
			}) //close stderr
			python.stdout.on('end', function() {
				fulfill(data)
			})
		}) // close Promise
	} // close create_vcf function
	dwnld()
})

// Listening //

var template = 'Node app is running at localhost: {port~number}'
var txt = template.replace('{port~number}', app.get('port'))

app.listen(app.get('port'), function() {
    console.log(txt)
})
