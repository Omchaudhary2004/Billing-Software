console.log("hello world")

async function getNumber() {
    let response = await fetch( 'test', {
        method: 'get',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With':'XMLHttpResquest'
        }
    })
    let data = await response.json()
    console.log(await data)
}