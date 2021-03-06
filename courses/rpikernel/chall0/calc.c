#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/proc_fs.h>
#include <asm/uaccess.h>

#define NAME "calc"

long m_add(long a, long b) {return a+b;}
long m_sub(long a, long b) {return a-b;}
long m_mul(long a, long b) {return a*b;}
long m_div(long a, long b) {return b == 0 ? LONG_MAX : a/b;}
long m_xor(long a, long b) {return a^b;}

// this function is called when writing to the proc entry
// e.g. int fd = open("/proc/calc", O_WRONLY); write(fd, "hi", 2);
static ssize_t proc_write(struct file* file, const char* buf, size_t len, loff_t* off) {
	long a, b;
	char op;
	if (sscanf(buf, "%ld%c%ld", &a, &op, &b) != 3) {
		printk(KERN_INFO "[x] wrong format: %s\n", buf);
		return -EINVAL;
	}
	long (*f)(long, long) = 0;
	switch (op) {
		case '+':
			f = m_add;
			break;
		case '-':
			f = m_sub;
			break;
		case '*':
			f = m_mul;
			break;
		case '/':
			f = m_div;
			break;
		case '^':
			f = m_xor;
			break;
		default:
			printk(KERN_INFO "[x] %c is not a valid op :(\n", op);
			break;
	}
	long res = f(a, b);
	printk(KERN_INFO "[+] %ld %c %ld = %ld\n", a, op, b, res);
	return len;
}

static const struct file_operations proc_ops = {
	.owner = THIS_MODULE,
	.write = proc_write

};

static int __init m_init(void) {
	struct proc_dir_entry* procfile = proc_create(NAME, 0666, 0, &proc_ops);
	if (!procfile) {
		printk(KERN_INFO "[!] couldnt create proc entry\n");
		return -ENOMEM;
	}
	printk(KERN_INFO "[+] calc module loaded\n");
	printk(KERN_INFO "[+] Outsource your tough mathematical operations to ring 0!\n");
	printk(KERN_INFO "[+] use like: echo '17*17' > /proc/calc\n");
	return 0;
}

static void __exit m_exit(void) {
	remove_proc_entry(NAME, 0);
	printk(KERN_INFO "[+] calc module unloaded\n");
}

MODULE_LICENSE("GPL");
module_init(m_init); // specifies which function is called when the module is loaded
module_exit(m_exit); // similarly, this is called when it's unloaded

