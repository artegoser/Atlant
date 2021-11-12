module.exports = async (manager, data)=>{

    console.log("parse ru questions");
    for(let i of Object.keys(data.questions.ru)){
        for(let item of data.questions.ru[i]) manager.addDocument('ru', item, i);
    }
    console.log("parsed ru questions...");

    console.log("parse en questions");
    for(let i of Object.keys(data.questions.en)){
        for(let item of data.questions.en[i]) manager.addDocument('en', item, i);
    }
    console.log("parsed en questions...");

    console.log("parse en answers");
    for(let i of Object.keys(data.answers.en)){
        for(let item of data.answers.en[i]) manager.addAnswer('en', i, item);
    }
    console.log("parsed en answers...");

    console.log("parse ru answers");
    for(let i of Object.keys(data.answers.ru)){
        for(let item of data.answers.ru[i]) manager.addAnswer('ru', i, item);
    }
    console.log("parsed ru answers...");

    await manager.train();
    manager.save(data.name+".nlp");
}