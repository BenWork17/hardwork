import jsonfile from "jsonfile";
import moment from "moment";
import simpleGit from "simple-git";
import random from "random";

const path = "./data.json";

const markCommit = async (x, y) => {
  try {
    const git = simpleGit();

    // base date set to 2025-01-02 (bỏ qua 2025-01-01 giống logic cũ)
    const base = moment().year(2025).startOf("year").add(1, "d");

    // clone base để không mutate object gốc nếu gọi nhiều lần
    const date = base.clone().add(x, "w").add(y, "d").format();

    const data = { date };

    // jsonfile.writeFile không trả promise mặc định -> bọc vào Promise
    await new Promise((resolve, reject) =>
      jsonfile.writeFile(path, data, (err) => (err ? reject(err) : resolve()))
    );

    // add, commit, push và chờ từng bước
    await git.add([path]);

    const commitResult = await git.commit(date, [path], { "--date": date });
    console.log("commit result:", commitResult);

    const pushResult = await git.push();
    console.log("push result:", pushResult);
  } catch (err) {
    console.error("Git operation failed:", err);
  }
};

// const makeCommits = (n) => {
//   if(n===0) return simpleGit().push();
//   const x = random.int(0, 54);
//   const y = random.int(0, 6);
//   const date = moment().subtract(1, "y").add(1, "d").add(x, "w").add(y, "d").format();

//   const data = {
//     date: date,
//   };
//   console.log(date);
//   jsonfile.writeFile(path, data, () => {
//     simpleGit().add([path]).commit(date, { "--date": date },makeCommits.bind(this,--n));
//   });
// };

markCommit(23, 0);
